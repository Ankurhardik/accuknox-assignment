-- ============================================================================
-- Complex Database Code Showcase: Multi-Tenant Telemetry & Advanced Analytics
-- Author: Ankur Hardik (https://github.com/AnkurHardik)
-- Engine: PostgreSQL 14+ / Compatible Relational Engines
-- Concepts Demonstrated:
--   1. Schema Normalization & Constraints (3NF, Check constraints, Foreign keys)
--   2. Indexing Strategies (Covering, Composite, Partial B-Tree indexes)
--   3. Advanced Window Functions (DENSE_RANK, LAG, LEAD, Cumulative sums)
--   4. Recursive Common Table Expressions (CTE) for Tree Traversal
--   5. Idempotent Upsert Operations & ACID Transaction Management
-- ============================================================================

BEGIN;

-- 1. SCHEMA DEFINITION WITH INTEGRITY CONSTRAINTS
CREATE TABLE IF NOT EXISTS tenants (
    tenant_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    plan_tier VARCHAR(20) NOT NULL CHECK (plan_tier IN ('Free', 'Standard', 'Enterprise')),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS security_events (
    event_id BIGSERIAL PRIMARY KEY,
    tenant_id VARCHAR(36) NOT NULL REFERENCES tenants(tenant_id) ON DELETE CASCADE,
    namespace VARCHAR(64) NOT NULL,
    pod_name VARCHAR(128) NOT NULL,
    event_type VARCHAR(64) NOT NULL, -- e.g. 'ProcessExec', 'NetworkConnect', 'FileModification'
    severity VARCHAR(16) NOT NULL CHECK (severity IN ('Low', 'Medium', 'High', 'Critical')),
    event_payload JSONB,
    occurred_at TIMESTAMPTZ NOT NULL,
    ingested_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Organization / Policy Hierarchy for Recursive Traversal
CREATE TABLE IF NOT EXISTS policy_groups (
    group_id SERIAL PRIMARY KEY,
    tenant_id VARCHAR(36) NOT NULL REFERENCES tenants(tenant_id),
    parent_group_id INTEGER REFERENCES policy_groups(group_id),
    name VARCHAR(100) NOT NULL,
    policy_action VARCHAR(20) NOT NULL CHECK (policy_action IN ('Audit', 'Block', 'Allow'))
);

-- 2. PERFORMANCE INDEXING STRATEGY
-- Composite B-Tree index for tenant + time-series range scans
CREATE INDEX IF NOT EXISTS idx_security_events_tenant_time 
ON security_events(tenant_id, occurred_at DESC);

-- Partial index for fast alert retrieval of High/Critical security incidents
CREATE INDEX IF NOT EXISTS idx_security_events_critical 
ON security_events(tenant_id, occurred_at DESC) 
WHERE severity IN ('High', 'Critical');

COMMIT;


-- ============================================================================
-- QUERY 1: Recursive CTE - Hierarchical Policy Inheritance Resolution
-- Resolves inherited security policies from Root group down to child namespaces.
-- ============================================================================
WITH RECURSIVE policy_hierarchy AS (
    -- Anchor member: Top-level root policy groups
    SELECT 
        group_id,
        tenant_id,
        parent_group_id,
        name AS group_path,
        policy_action,
        1 AS hierarchy_depth
    FROM policy_groups
    WHERE parent_group_id IS NULL

    UNION ALL

    -- Recursive member: Traverse child groups inheriting parent actions
    SELECT 
        child.group_id,
        child.tenant_id,
        child.parent_group_id,
        parent.group_path || ' -> ' || child.name AS group_path,
        COALESCE(child.policy_action, parent.policy_action) AS policy_action,
        parent.hierarchy_depth + 1 AS hierarchy_depth
    FROM policy_groups child
    INNER JOIN policy_hierarchy parent 
        ON child.parent_group_id = parent.group_id
)
SELECT 
    group_id,
    tenant_id,
    group_path,
    policy_action,
    hierarchy_depth
FROM policy_hierarchy
ORDER BY tenant_id, hierarchy_depth, group_path;


-- ============================================================================
-- QUERY 2: Multi-Window Analytics - Rolling Incident Spike Detection
-- Calculates 1-hour event velocity, inter-arrival time using LAG, and dense rank
-- to isolate abnormal bursts of critical security events per pod.
-- ============================================================================
WITH ranked_incident_stream AS (
    SELECT 
        event_id,
        tenant_id,
        namespace,
        pod_name,
        severity,
        occurred_at,
        -- Inter-event latency (difference in seconds from previous event on same pod)
        EXTRACT(EPOCH FROM (occurred_at - LAG(occurred_at) OVER (
            PARTITION BY tenant_id, pod_name 
            ORDER BY occurred_at
        ))) AS seconds_since_prior_event,
        -- Running cumulative count of critical events in the observation partition
        COUNT(CASE WHEN severity = 'Critical' THEN 1 END) OVER (
            PARTITION BY tenant_id, pod_name 
            ORDER BY occurred_at 
            ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
        ) AS rolling_critical_burst_count,
        -- Dense rank of pods by volume of critical incidents within each namespace
        DENSE_RANK() OVER (
            PARTITION BY tenant_id, namespace 
            ORDER BY occurred_at DESC
        ) AS recency_rank
    FROM security_events
    WHERE occurred_at >= NOW() - INTERVAL '24 hours'
)
SELECT 
    tenant_id,
    namespace,
    pod_name,
    event_id,
    occurred_at,
    ROUND(seconds_since_prior_event::numeric, 2) AS inter_arrival_sec,
    rolling_critical_burst_count,
    CASE 
        WHEN rolling_critical_burst_count >= 3 AND seconds_since_prior_event < 5.0 
        THEN 'ACTIVE_EXPLOIT_BURST'
        WHEN rolling_critical_burst_count >= 1 
        THEN 'MONITOR_ELEVATED'
        ELSE 'BASELINE'
    END AS anomaly_classification
FROM ranked_incident_stream
WHERE recency_rank <= 100
ORDER BY tenant_id, namespace, occurred_at DESC;
