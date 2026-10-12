# Problem Statement 1: Practical Engineering & Code

This directory contains the implementations, test datasets, and entry points for the three practical coding tasks in the AccuKnox assessment.

---

## 📂 Subdirectories

- **[`task1_api_to_db/`](./task1_api_to_db)**: Fetches books from external REST API, normalizes data, and executes idempotent upsert into SQLite.
  - Run via: `uv run python Problem_Statement_1/task1_api_to_db/run.py`
- **[`task2_data_viz/`](./task2_data_viz)**: Processes student test scores, computes descriptive cohort benchmarks, and exports a dual-panel bar chart (`student_scores_visualization.png`).
  - Run via: `uv run python Problem_Statement_1/task2_data_viz/run.py`
- **[`task3_csv_import/`](./task3_csv_import)**: Parses user CSV data, performs RFC regex email validation, handles dirty records, logs rejections, and performs batch upsert into SQLite.
  - Run via: `uv run python Problem_Statement_1/task3_csv_import/run.py`
- **[`code_showcase/`](./code_showcase)**: Documentation and code links for Tasks 4 & 5 (Most complex Python and Database code written by Ankur Hardik).

---

## ⚡ Quickstart (Run All at Once)

From the project root:
```bash
uv run python run_all_tasks.py
```
