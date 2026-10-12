# Problem Statement 2: Subjective Research & Architecture

This folder contains the in-depth architectural and conceptual responses for **Assignment 2** of the AccuKnox AI/ML Trainee assessment.

---

## 📑 Contents

1. [01_self_rating.md](./01_self_rating.md)
   - Evaluated self-ratings across **ML, AI, Deep Learning, and LLM** based on the `[A, B, C]` scale.
   - Grounded with real-world project experience (XGBoost Churn Prediction, RAG, and Agentic systems).

2. [02_llm_chatbot_architecture.md](./02_llm_chatbot_architecture.md)
   - 6-Layer enterprise LLM chatbot architecture.
   - Covers client streaming (SSE), session memory buffers, hybrid RAG (dense + sparse), cross-encoder re-ranking, prompt orchestration, and the RAG Triad observability framework.

3. [03_vector_databases_and_qdrant.md](./03_vector_databases_and_qdrant.md)
   - Vector database fundamentals (embeddings, Cosine vs. L2 distance, HNSW graphs vs. IVF-PQ).
   - Defined hypothetical scenario: **Real-Time Security Threat & Incident Matching for Kubernetes (KubeArmor Telemetry)**.
   - Justification for selecting **Qdrant** (Rust engine, payload-aware HNSW, on-premise Zero Trust compliance).
   - Head-to-head comparison matrix against Pinecone, Milvus, and Chroma.
