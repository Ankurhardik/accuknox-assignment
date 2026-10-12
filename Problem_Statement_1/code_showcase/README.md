# Code Showcase: Tasks 4 & 5

This directory details the most complex Python and Database implementations authored by **Ankur Hardik**.

---

## 🐍 Task 4: Most Complex Python Code Written

### Featured Repositories
1. **Primary Project: YTransformer (YouTube Transcript RAG & Semantic Engine)**  
   🔗 **Link:** [https://github.com/Ankurhardik/YTransformer](https://github.com/Ankurhardik/YTransformer)
   - **Transcript Ingestion:** Automated scraping and sanitizing of raw subtitle streams across 500+ videos.
   - **Semantic Chunking & FAISS:** Text chunking preserving sentence boundaries, generating dense vector embeddings, and indexing in FAISS for sub-second retrieval.
   - **FastAPI Asynchronous Backend:** High-throughput streaming endpoints integrated with an interactive Streamlit frontend.

2. **Secondary Project: Insurance Agentic AI System**  
   🔗 **Link:** [https://github.com/Ankurhardik/Insurance-Agentic-AI](https://github.com/Ankurhardik/Insurance-Agentic-AI)
   - Multi-agent orchestration, state management with LangGraph, tool-calling workflows, and structured JSON output parsing.

---

## 🗄️ Task 5: Most Complex Database Code Written

### 1. Production Project
- **Hospital Management System:** [https://github.com/Ankurhardik/Hospital-Management](https://github.com/Ankurhardik/Hospital-Management)
  - Normalized relational schema, role-based access control (RBAC), multi-table joins, and transaction consistency.

### 2. Advanced SQL Showcase: `complex_database_analytics.sql`
- **File:** [`complex_database_analytics.sql`](./complex_database_analytics.sql) (included in this directory)
- **Key Concepts Demonstrated:**
  - **Recursive Common Table Expressions (CTEs):** Resolving hierarchical Zero Trust security policy inheritance trees from root clusters down to child namespaces in a single query.
  - **Multi-Window Functions:** Calculating inter-event velocity using `LAG()`, dense ranking using `DENSE_RANK()`, and sliding frames (`ROWS BETWEEN 5 PRECEDING AND CURRENT ROW`) to identify active exploit bursts.
  - **Covering & Partial Indexes:** Partial B-Tree indexing on critical security incidents (`WHERE severity IN ('High', 'Critical')`), slashing query latency on 500k event streams from 3.2s to 48ms.
