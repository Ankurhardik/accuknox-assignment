#!/usr/bin/env python3
"""
Entry point for Task 3: CSV Data Import to SQLite.
Run directly via: python run.py
"""
import os
import sys

# Ensure module path resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Problem_Statement_1.task3_csv_import.csv_importer import UserCSVImporter

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    csv_file = os.path.join(current_dir, "users.csv")
    db_file = os.path.join(current_dir, "users_directory.db")
    
    importer = UserCSVImporter(csv_path=csv_file, db_path=db_file)
    importer.run()
