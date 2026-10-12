# AccuKnox AI/ML Trainee Technical Assessment

**Candidate:** Ankur Hardik  
**Institute:** Birla Institute of Technology, Mesra (B.Tech ECE, CGPA: 8.19)  
**Email:** ankurhardik123@gmail.com | **Phone:** +91-6207084400  
**GitHub:** [https://github.com/AnkurHardik](https://github.com/AnkurHardik) | **Portfolio:** [https://ankurhardik.vercel.app/](https://ankurhardik.vercel.app/)  

---

## 🚀 Overview

This repository contains the complete, production-grade solutions for the **AccuKnox AI/ML Trainee Assessment**. 

The project is structured in a **clean, modular architecture** adhering to modern Python standards with **`uv` package management**, atomic database operations, real-world data sanitation, publication-ready data visualizations, and in-depth architectural research into LLM chatbots and **Qdrant** vector databases.

---

## ⚡ Quickstart with `uv`

This project uses [`uv`](https://docs.astral.sh/uv/) for high-speed, reproducible Python package and environment management.

### 1. Install `uv` (if not already installed)
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Run All Tasks with One Command
```bash
uv run python run_all_tasks.py
```

### 3. Run Individual Modular Tasks
```bash
# Task 1: API Data Retrieval & SQLite Persistence
uv run python Problem_Statement_1/task1_api_to_db/run.py

# Task 2: Student Test Scores Processing & Bar Chart
uv run python Problem_Statement_1/task2_data_viz/run.py

# Task 3: CSV Data Import & Email Sanitation
uv run python Problem_Statement_1/task3_csv_import/run.py
```

---

## 📁 Repository Structure

```
accuknox-assignment/
├── README.md                                          <- Main repository documentation
├── pyproject.toml                                     <- Modern uv project configuration
├── uv.lock                                            <- Deterministic dependency lockfile
├── requirements.txt                                   <- Pip-compatible fallback requirements
├── run_all_tasks.py                                   <- Master one-click task runner
│
├── Ankur_Hardik_AccuKnox_AI_ML_Assessment.docx       <- Official submission Word document
├── Ankur_Hardik_Resume.pdf                            <- Candidate resume (PDF)
│
├── Problem_Statement_1/                               <- Practical Code & Engineering
│   ├── README.md
│   ├── task1_api_to_db/
│   │   ├── __init__.py
│   │   ├── books_etl.py                               <- REST API fetcher & idempotent SQLite upsert
│   │   └── run.py                                     <- Entry point
│   ├── task2_data_viz/
│   │   ├── __init__.py
│   │   ├── students_scores.json                       <- Input dataset
│   │   ├── score_processor.py                         <- Statistical analysis & chart rendering
│   │   ├── student_scores_visualization.png           <- Generated 300 DPI bar chart
│   │   └── run.py                                     <- Entry point
│   ├── task3_csv_import/
│   │   ├── __init__.py
│   │   ├── users.csv                                  <- CSV dataset with real-world edge cases
│   │   ├── csv_importer.py                            <- Regex email validation & batch upsert
│   │   └── run.py                                     <- Entry point
│   └── code_showcase/
│       ├── README.md                                  <- Detailed descriptions for Tasks 4 & 5
│       └── complex_database_analytics.sql             <- Advanced PostgreSQL CTEs & Window functions
│
└── Problem_Statement_2/                               <- Subjective Architecture & Research
    ├── README.md
    ├── 01_self_rating.md                              <- Calibrated ratings across ML, AI, DL, and LLMs
    ├── 02_llm_chatbot_architecture.md                 <- 6-Layer enterprise chatbot architecture
    └── 03_vector_databases_and_qdrant.md              <- Vector DB deep dive & Qdrant K8s evaluation
```

---

## 🛠️ Summary of Implementations

### Problem Statement 1: Practical Engineering
1. **Task 1 (API $\rightarrow$ SQLite):** Ingests book data, handles network timeouts and rate-limiting gracefully with offline fallback, enforces `UNIQUE(book_key)` with `INSERT ... ON CONFLICT DO UPDATE`, and indexes publication year.
2. **Task 2 (Data Processing & Visualization):** Calculates student averages, subject averages, and class mean. Exports a dual-panel visualization (`student_scores_visualization.png`) featuring semantic color coding (Steel Blue for above-average, Warm Coral for below-average) and direct score callouts.
3. **Task 3 (CSV $\rightarrow$ SQLite):** Defensively handles dirty data by validating RFC-compliant email formats with regex, strips whitespace, records rejected rows in an audit log, and executes batch upserts.
4. **Task 4 (Most Complex Python Code):** Showcases [YTransformer](https://github.com/Ankurhardik/YTransformer) (YouTube RAG pipeline with FAISS, FastAPI, and Streamlit) and [Insurance-Agentic-AI](https://github.com/Ankurhardik/Insurance-Agentic-AI).
5. **Task 5 (Most Complex Database Code):** Showcases [Hospital-Management](https://github.com/Ankurhardik/Hospital-Management) and [`complex_database_analytics.sql`](./Problem_Statement_1/code_showcase/complex_database_analytics.sql) featuring recursive CTEs for Zero Trust policy hierarchy traversal and multi-window anomaly burst detection (`LAG()`, `DENSE_RANK()`).

---

### Problem Statement 2: Architecture & Research
1. **Question 1 (Self-Rating):** Honest, calibrated self-assessment (**ML: A**, **AI: A**, **Deep Learning: B**, **LLMs: B+**) backed by real project achievements.
2. **Question 2 (LLM Chatbot Architecture):** Comprehensive 6-layer design covering SSE token streaming, token-budgeted memory buffers, hybrid RAG (dense vector + sparse BM25) with cross-encoder re-ranking, prompt orchestration, and the RAG Triad observability framework.
3. **Question 3 (Vector Databases & Qdrant):** First-principles mathematical explanation (Cosine, Euclidean, HNSW, IVF-PQ). Defines a real-world scenario: **"Real-Time Threat Intelligence Matching over Kubernetes Runtime Audit Logs (KubeArmor Telemetry)"**. Defends the selection of **Qdrant** (Rust engine, payload-aware HNSW single-stage filtering, and on-premise Zero Trust fit) with a head-to-head comparison matrix against Pinecone, Milvus, and Chroma.

---

## 📄 Submission Files

- **Official Word Submission:** [`Ankur_Hardik_AccuKnox_AI_ML_Assessment.docx`](./Ankur_Hardik_AccuKnox_AI_ML_Assessment.docx)
- **Candidate Resume:** [`Ankur_Hardik_Resume.pdf`](./Ankur_Hardik_Resume.pdf)
