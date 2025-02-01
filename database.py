import sqlite3
import datetime

def init_db():
    with sqlite3.connect("salary.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time TEXT,
                end_time TEXT,
                total_salary REAL
            )
        """)
        conn.commit()

def add_shift(start_time, end_time, total_salary):
    """Insert shift record into database."""
    with sqlite3.connect("salary.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO shifts (start_time, end_time, total_salary) VALUES (?, ?, ?)",
                       (start_time, end_time, total_salary))
        conn.commit()


def get_all_shifts():
    """Retrieve all shift records."""
    with sqlite3.connect("salary.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, start_time, end_time, total_salary FROM shifts ORDER BY id DESC")
        shifts = cursor.fetchall()

    return [{"id": s[0], "start_time": s[1], "end_time": s[2], "total_salary": s[3]} for s in shifts]
