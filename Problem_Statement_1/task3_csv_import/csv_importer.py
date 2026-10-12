"""
Module: csv_importer.py
Package: Problem_Statement_1.task3_csv_import

Ingests user records from CSV, sanitizes dirty fields, performs RFC regex
email validation, and executes atomic upsert transactions into SQLite.
"""

import csv
import logging
import re
import sqlite3
from typing import List, Dict, Tuple

logger = logging.getLogger("UserCSVImporter")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


class UserCSVImporter:
    def __init__(self, csv_path: str = "users.csv", db_path: str = "users_directory.db"):
        self.csv_path = csv_path
        self.db_path = db_path

    def init_database(self) -> None:
        """Initializes SQLite schema with index on email."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    role TEXT DEFAULT 'User',
                    imported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
            """)
            conn.commit()

    @staticmethod
    def validate_and_clean_row(row: Dict[str, str], line_num: int) -> Tuple[bool, str, Dict[str, str]]:
        """Cleans and validates each CSV row."""
        name = (row.get("name") or "").strip()
        email = (row.get("email") or "").strip().lower()
        role = (row.get("role") or "User").strip()

        if not name:
            return False, f"Line {line_num}: Missing or empty 'name' field.", {}
        if not email:
            return False, f"Line {line_num}: Missing or empty 'email' field.", {}
        if not EMAIL_REGEX.match(email):
            return False, f"Line {line_num}: Invalid email format '{email}'.", {}

        return True, "", {"name": name, "email": email, "role": role}

    def import_records(self) -> Tuple[int, List[str]]:
        """Parses CSV and executes batch upsert."""
        valid_records = []
        rejections = []

        with open(self.csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for line_idx, row in enumerate(reader, start=2):
                is_valid, reason, clean_data = self.validate_and_clean_row(row, line_idx)
                if is_valid:
                    valid_records.append((clean_data["name"], clean_data["email"], clean_data["role"]))
                else:
                    rejections.append(reason)

        upsert_sql = """
            INSERT INTO users (name, email, role)
            VALUES (?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
                name = excluded.name,
                role = excluded.role,
                imported_at = CURRENT_TIMESTAMP;
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(upsert_sql, valid_records)
            conn.commit()

        return len(valid_records), rejections

    def display(self) -> None:
        """Displays stored user records."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, role, imported_at FROM users ORDER BY id ASC;")
            rows = cursor.fetchall()

        print("\n" + "=" * 80)
        print("                    DATABASE USER RECORDS (SQLITE)                    ")
        print("=" * 80)
        print(f"{'ID':<4} | {'NAME':<20} | {'EMAIL':<30} | {'ROLE':<18}")
        print("-" * 80)
        for r in rows:
            user_id, name, email, role, _ = r
            print(f"{user_id:<4} | {name:<20} | {email:<30} | {role:<18}")
        print("=" * 80)
        print(f"Total Unique Users in Database: {len(rows)}\n")

    def run(self) -> None:
        """Executes full ingestion workflow."""
        self.init_database()
        success_count, rejections = self.import_records()
        self.display()

        if rejections:
            print("Data Quality & Sanitation Audit Log:")
            for r in rejections:
                print(f"  [SKIPPED] {r}")
            print()
