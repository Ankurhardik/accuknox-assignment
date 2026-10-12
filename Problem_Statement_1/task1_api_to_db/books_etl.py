"""
Module: books_etl.py
Package: Problem_Statement_1.task1_api_to_db

Fetches book information from an external REST API, normalizes records,
and persists them into a local SQLite database using idempotent upsert operations.
"""

import json
import logging
import sqlite3
import urllib.request
import urllib.error
from typing import List, Dict, Any

logger = logging.getLogger("BooksETL")


class BooksETLPipeline:
    def __init__(
        self,
        db_path: str = "books_library.db",
        api_url: str = "https://openlibrary.org/search.json?q=artificial+intelligence&limit=10"
    ):
        self.db_path = db_path
        self.api_url = api_url

    def init_database(self) -> None:
        """Initializes SQLite schema with indexes and uniqueness constraints."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_key TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    publication_year INTEGER,
                    isbn TEXT,
                    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_books_year ON books(publication_year);
            """)
            conn.commit()
        logger.info("Database schema initialized at '%s'.", self.db_path)

    def fetch_records(self) -> List[Dict[str, Any]]:
        """Fetches books from REST API with resilient local fallback."""
        logger.info("Querying REST API endpoint: %s", self.api_url)
        headers = {"User-Agent": "AccuKnox-AIML-Candidate-Evaluation/1.0"}
        req = urllib.request.Request(self.api_url, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    payload = json.loads(response.read().decode("utf-8"))
                    docs = payload.get("docs", [])
                    logger.info("Successfully received %d records from remote API.", len(docs))
                    return docs
        except Exception as err:
            logger.warning("Remote API unavailable (%s). Activating resilient offline payload.", err)

        # Fallback offline payload for reliable execution
        return [
            {
                "key": "/works/OL1001",
                "title": "Artificial Intelligence: A Modern Approach",
                "author_name": ["Stuart Russell", "Peter Norvig"],
                "first_publish_year": 1995,
                "isbn": ["9780136042594"]
            },
            {
                "key": "/works/OL1002",
                "title": "Deep Learning",
                "author_name": ["Ian Goodfellow", "Yoshua Bengio", "Aaron Courville"],
                "first_publish_year": 2016,
                "isbn": ["9780262035613"]
            },
            {
                "key": "/works/OL1003",
                "title": "Pattern Recognition and Machine Learning",
                "author_name": ["Christopher M. Bishop"],
                "first_publish_year": 2006,
                "isbn": ["9780387310732"]
            },
            {
                "key": "/works/OL1004",
                "title": "Reinforcement Learning: An Introduction",
                "author_name": ["Richard S. Sutton", "Andrew G. Barto"],
                "first_publish_year": 1998,
                "isbn": ["9780262193986"]
            },
            {
                "key": "/works/OL1005",
                "title": "The Hundred-Page Machine Learning Book",
                "author_name": ["Andriy Burkov"],
                "first_publish_year": 2019,
                "isbn": ["9781999570507"]
            }
        ]

    def transform_and_store(self, raw_books: List[Dict[str, Any]]) -> int:
        """Transforms raw JSON into sanitized tuples and executes idempotent upsert."""
        clean_records = []
        for item in raw_books:
            book_key = item.get("key") or item.get("id") or str(hash(item.get("title", "")))
            title = (item.get("title") or "Unknown Title").strip()
            
            authors = item.get("author_name") or item.get("author") or ["Unknown Author"]
            author_str = ", ".join(authors) if isinstance(authors, list) else str(authors)
            
            pub_year = item.get("first_publish_year") or item.get("publication_year")
            try:
                pub_year = int(pub_year) if pub_year is not None else None
            except (ValueError, TypeError):
                pub_year = None
                
            isbns = item.get("isbn") or []
            first_isbn = isbns[0] if isinstance(isbns, list) and isbns else (isbns if isinstance(isbns, str) else None)
            
            clean_records.append((book_key, title, author_str, pub_year, first_isbn))

        upsert_query = """
            INSERT INTO books (book_key, title, author, publication_year, isbn)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(book_key) DO UPDATE SET
                title = excluded.title,
                author = excluded.author,
                publication_year = excluded.publication_year,
                isbn = excluded.isbn,
                fetched_at = CURRENT_TIMESTAMP;
        """

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(upsert_query, clean_records)
            conn.commit()

        logger.info("Persisted %d records into SQLite.", len(clean_records))
        return len(clean_records)

    def fetch_stored_books(self) -> List[tuple]:
        """Retrieves books from database sorted by publication year."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, title, author, publication_year, isbn, fetched_at
                FROM books
                ORDER BY publication_year ASC NULLS LAST;
            """)
            return cursor.fetchall()

    def display(self) -> None:
        """Prints a clean tabular display of stored books."""
        rows = self.fetch_stored_books()
        print("\n" + "=" * 95)
        print(f"{'ID':<4} | {'TITLE':<36} | {'AUTHOR':<26} | {'YEAR':<5} | {'ISBN':<13}")
        print("=" * 95)
        for r in rows:
            book_id, title, author, year, isbn, _ = r
            short_title = (title[:33] + "...") if len(title) > 36 else title
            short_author = (author[:23] + "...") if len(author) > 26 else author
            year_str = str(year) if year else "N/A"
            isbn_str = str(isbn)[:13] if isbn else "N/A"
            print(f"{book_id:<4} | {short_title:<36} | {short_author:<26} | {year_str:<5} | {isbn_str:<13}")
        print("=" * 95)
        print(f"Total Books in SQLite: {len(rows)}\n")

    def run(self) -> None:
        """Executes full ETL lifecycle."""
        self.init_database()
        raw_data = self.fetch_records()
        self.transform_and_store(raw_data)
        self.display()
