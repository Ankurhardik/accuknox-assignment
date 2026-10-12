#!/usr/bin/env python3
"""
Entry point for Task 1: API Data Retrieval and Storage.
Run directly via: python run.py
"""
import os
import sys

# Ensure module path resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Problem_Statement_1.task1_api_to_db.books_etl import BooksETLPipeline

if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(__file__), "books_library.db")
    pipeline = BooksETLPipeline(db_path=db_file)
    pipeline.run()
