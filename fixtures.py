"""fixtures.py — Predefined habits with 4 weeks of example completion data."""

from datetime import datetime, timedelta
from manager import HabitManager

def init_fixtures(manager: HabitManager):
    """
    Create 5 predefined habits (3 daily, 2 weekly) with 4 weeks of completion data.
    """
    predefined_habits = [
        ("Brush Teeth", "daily"),
        ("Exercise", "daily"),
        ("Read", "daily"),
        ("Grocery Shopping", "weekly"),
        ("Call Family", "weekly"),
    ]

    # Delete existing habits with same names (avoid duplicates)
    for name, _ in predefined_habits:
        try:
            manager.delete_habit(name)
        except Exception:
            pass

    today = datetime.now().date()

    # Create and populate example habits
    for name, period in predefined_habits:
        habit = manager.create_habit(name, period)

        if period == "daily":
            # Simulate 4 weeks of daily completions (with some skipped days)
            for i in range(28):
                if i % 6 != 0:  # skip every 6th day
                    dt = datetime.combine(today - timedelta(days=i), datetime.min.time())
                    habit.complete(dt)
        else:
            # Weekly habits - mark one completion per week for 4 weeks
            for week in range(4):
                dt = datetime.combine(today - timedelta(weeks=week), datetime.min.time())
                habit.complete(dt)

        manager.storage.save(habit)

    print("✅ Example habits have been created successfully.")