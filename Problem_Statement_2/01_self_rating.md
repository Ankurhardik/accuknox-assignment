# Question 1: Self-Rating & Technical Grounding

**Candidate:** Ankur Hardik  
**Institute:** Birla Institute of Technology, Mesra  
**Evaluation Rubric:**  
* `A` = Can code independently  
* `B` = Can code under supervision  
* `C` = Little or no understanding  

---

## 1. Summary Evaluation Matrix

| Domain | Rating | Practical Justification & Real-World Grounding |
| :--- | :---: | :--- |
| **Machine Learning (ML)** | **A** | **Can code independently.** Complete end-to-end pipelines: EDA, data preprocessing, feature engineering, and model training (Random Forests, Gradient Boosting via XGBoost/LightGBM, SVMs) using `scikit-learn`. Validated by my *Customer Churn Prediction* project achieving an **AUC-ROC of 0.91** across 10,000+ records with **SHAP interpretability** analysis. |
| **Artificial Intelligence (AI)** | **A** | **Can code independently.** Strong algorithmic foundation in classical AI search: heuristic optimization ($A^*$, Minimax with Alpha-Beta pruning), decision logic, constraint satisfaction, and rule-based systems. Experienced in translating discrete problem requirements into graph traversals and algorithmic Python. |
| **Deep Learning (DL)** | **B** | **Can code under supervision.** Hands-on implementation of CNNs, LSTMs, and Transformers using `PyTorch`. Capable of defining custom loss functions, learning rate schedules, and transfer learning on pre-trained backbones. Would value senior guidance on distributed multi-GPU training (DDP/FSDP) and low-level CUDA optimization. |
| **Large Language Models (LLM)** | **B+** | **Application-Level: A (Independent) \| Model-Level: B (Supervised)**<br>• **Application Level (A):** Independently design and deploy RAG pipelines, LangChain/LlamaIndex workflows, vector database retrieval (FAISS, Chroma, Qdrant), and prompt orchestration. Proven in my *YouTube RAG Chatbot* and *Resume-Job Matching System*.<br>• **Model Level (B):** Fine-tuning open weights (LLaMA-2/Mistral via LoRA/QLoRA) is within my capability; pretraining from scratch requires senior supervision. |

---

## 2. In-Depth Technical Justifications

### 🔹 Machine Learning (Rating: A)
- **Hands-on Scope:** Confident with the full lifecycle from hypothesis formulation to model evaluation. Capable of handling skewed target distributions using SMOTE, stratified $k$-fold cross-validation, and optimizing precision-recall curves.
- **Evidence:** Built an automated churn prediction system benchmarking Logistic Regression, Random Forest, and XGBoost. Interpreted feature importance using TreeSHAP to reveal key business drivers.

### 🔹 Artificial Intelligence (Rating: A)
- **Hands-on Scope:** Deep understanding of classical state-space search, heuristic pruning, and game-tree algorithms. Adept at designing deterministic decision engines and multi-agent coordination.
- **Evidence:** Academic coursework and algorithmic projects at BIT Mesra, implementing pathfinding algorithms, constraint propagation, and rule-based workflow automations (e.g., placement notification bots).

### 🔹 Deep Learning (Rating: B)
- **Hands-on Scope:** Comfortable writing PyTorch training loops, managing forward/backward passes, zeroing gradients, and avoiding data leakage. Applied CNNs for computer vision tasks and tokenizers/embeddings for NLP.
- **Learning Horizon:** Eager to collaborate with senior ML engineers on distributed gradient synchronization, ZeRO stages in DeepSpeed, and tensor parallel inference.

### 🔹 Large Language Models (Rating: B+)
- **Hands-on Scope:** Built production-ready RAG applications using LangChain, Hugging Face transformers, and vector databases. Certified in *LangChain for LLM Application Development* and *Building Agentic RAG with LlamaIndex* by DeepLearning.AI.
- **Learning Horizon:** Expanding knowledge in Quantized Low-Rank Adaptation (QLoRA), alignment techniques (DPO/RLHF), and high-throughput inference serving via vLLM and TensorRT-LLM.
