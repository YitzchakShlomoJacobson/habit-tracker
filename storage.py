"""storage.py — SQLite persistence layer."""

import sqlite3
import os
from datetime import datetime
from typing import List
from habit import Habit

# The database file will be created in the same folder as this script
DB_FILE = os.path.join(os.path.dirname(__file__), "habits.db")

class Storage:
    """Handles saving and loading habits using SQLite."""

    def __init__(self, db_path=None):
        self.db_path = db_path or DB_FILE
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._init_db()

    def _init_db(self):
        """Create tables if they don't already exist."""
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                periodicity TEXT,
                created_at TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER,
                completed_at TEXT,
                FOREIGN KEY(habit_id) REFERENCES habits(id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()

    def save(self, habit: Habit):
        """Save or update a habit and its completion history."""
        cur = self.conn.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO habits (name, periodicity, created_at) VALUES (?, ?, ?)",
            (habit.name, habit.periodicity, habit.created_at.isoformat())
        )
        self.conn.commit()

        cur.execute("SELECT id FROM habits WHERE name=?", (habit.name,))
        hid = cur.fetchone()[0]

        # Remove old completions
        cur.execute("DELETE FROM completions WHERE habit_id=?", (hid,))
        # Insert all completions again
        for c in habit.completions:
            cur.execute(
                "INSERT INTO completions (habit_id, completed_at) VALUES (?, ?)",
                (hid, c.isoformat())
            )
        self.conn.commit()

    def load_all(self) -> List[Habit]:
        """Load all habits and their completions from the database."""
        cur = self.conn.cursor()
        cur.execute("SELECT id, name, periodicity, created_at FROM habits")
        rows = cur.fetchall()

        habits = []
        for hid, name, per, created_at in rows:
            cur.execute("SELECT completed_at FROM completions WHERE habit_id=?", (hid,))
            comps = [datetime.fromisoformat(r[0]) for r in cur.fetchall()]
            h = Habit(name, per)
            h.created_at = datetime.fromisoformat(created_at)
            h.completions = comps
            habits.append(h)
        return habits