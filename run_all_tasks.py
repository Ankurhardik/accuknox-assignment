#!/usr/bin/env python3
"""
Master Runner Script
====================
Runs all Problem Statement 1 practical tasks sequentially in a unified,
clean console dashboard.

Usage:
    uv run python run_all_tasks.py
"""

import sys
import os

# Ensure package imports resolve properly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from Problem_Statement_1.task1_api_to_db.books_etl import BooksETLPipeline
from Problem_Statement_1.task2_data_viz.score_processor import StudentScoreProcessor
from Problem_Statement_1.task3_csv_import.csv_importer import UserCSVImporter


def print_banner(title: str):
    print("\n" + "#" * 80)
    print(f"  {title.upper()}")
    print("#" * 80)


def main():
    print("\n" + "=" * 80)
    print("      ACCUKNOX AI/ML TRAINEE TECHNICAL ASSESSMENT - MASTER TASK RUNNER     ")
    print("      Candidate: Ankur Hardik | Environment: Python via 'uv'               ")
    print("=" * 80)

    # 1. RUN TASK 1
    print_banner("Running Task 1: API Data Retrieval & SQLite Persistence")
    db1_path = os.path.join("Problem_Statement_1", "task1_api_to_db", "books_library.db")
    t1 = BooksETLPipeline(db_path=db1_path)
    t1.run()

    # 2. RUN TASK 2
    print_banner("Running Task 2: Student Test Scores Processing & Visualization")
    json2_path = os.path.join("Problem_Statement_1", "task2_data_viz", "students_scores.json")
    img2_path = os.path.join("Problem_Statement_1", "task2_data_viz", "student_scores_visualization.png")
    t2 = StudentScoreProcessor(data_path=json2_path, output_image=img2_path)
    t2.run()

    # 3. RUN TASK 3
    print_banner("Running Task 3: CSV Data Ingestion & Sanitation Pipeline")
    csv3_path = os.path.join("Problem_Statement_1", "task3_csv_import", "users.csv")
    db3_path = os.path.join("Problem_Statement_1", "task3_csv_import", "users_directory.db")
    t3 = UserCSVImporter(csv_path=csv3_path, db_path=db3_path)
    t3.run()

    print("\n" + "=" * 80)
    print("  SUCCESS: All practical tasks executed cleanly with 0 errors!")
    print("  Artifacts Generated:")
    print(f"    • SQLite Books DB : {db1_path}")
    print(f"    • Matplotlib Chart: {img2_path}")
    print(f"    • SQLite Users DB : {db3_path}")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
