"""habit.py
Habit class representing a single habit and its completion events.
"""

from datetime import datetime, timedelta
from typing import List, Optional, Tuple


class Habit:
    """
    Represents a habit with events (completion timestamps).
    """

    def __init__(self, name: str, periodicity: str):
        if periodicity not in ("daily", "weekly"):
            raise ValueError("periodicity must be 'daily' or 'weekly'")
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions: List[datetime] = []

    def complete(self, when: Optional[datetime] = None):
        """Record a completion event (timestamp)."""
        when = when or datetime.now()
        self.completions.append(when)

    def get_streak(self, as_of: Optional[datetime] = None) -> int:
        """Calculate current streak (daily or weekly)."""
        if not self.completions:
            return 0
        as_of = as_of or datetime.now()
        from datetime import date
        comps = sorted(self.completions, reverse=True)
        streak = 0
        if self.periodicity == "daily":
            seen = {c.date() for c in comps}
            d = as_of.date()
            while d in seen:
                streak += 1
                d -= timedelta(days=1)
        else:
            seen_weeks = {(c.date().isocalendar()[0], c.date().isocalendar()[1]) for c in comps}
            y, w, _ = as_of.isocalendar()
            while (y, w) in seen_weeks:
                streak += 1
                w -= 1
                if w == 0:
                    y -= 1
                    w = 52
        return streak

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [c.isoformat() for c in self.completions],
        }

    @classmethod
    def from_dict(cls, d):
        h = cls(d["name"], d["periodicity"])
        from datetime import datetime
        h.created_at = datetime.fromisoformat(d["created_at"])
        h.completions = [datetime.fromisoformat(x) for x in d.get("completions", [])]
        return h