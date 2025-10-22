"""manager.py — Business logic for managing habits."""

from storage import Storage
from habit import Habit

class HabitManager:
    """Handles all habit-related operations: creating, listing, completing, and deleting habits."""

    def __init__(self):
        """Load all habits from the database when the manager starts."""
        self.storage = Storage()
        self.habits = self.storage.load_all()

    def create_habit(self, name: str, periodicity: str) -> Habit:
        """Create a new habit (daily or weekly)."""
        if any(h.name == name for h in self.habits):
            raise ValueError("A habit with this name already exists.")
        habit = Habit(name, periodicity)
        self.habits.append(habit)
        self.storage.save(habit)
        return habit

    def list_habits(self):
        """Return all tracked habits."""
        return self.habits

    def find(self, name: str):
        """Find a habit by its name."""
        for h in self.habits:
            if h.name.lower() == name.lower():
                return h
        return None

    def complete_habit(self, name: str):
        """Mark a habit as completed."""
        habit = self.find(name)
        if not habit:
            raise ValueError("Habit not found.")
        habit.complete()
        self.storage.save(habit)
        return habit

    def delete_habit(self, name: str) -> bool:
        """Delete a habit by name."""
        habit = self.find(name)
        if not habit:
            return False
        self.habits.remove(habit)
        cur = self.storage.conn.cursor()
        cur.execute("DELETE FROM habits WHERE name=?", (name,))
        self.storage.conn.commit()
        return True