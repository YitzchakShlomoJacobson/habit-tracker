"""analytics.py — Pure functions for analyzing habits using functional programming."""

from functools import reduce
from typing import List, Tuple, Optional
from habit import Habit


def list_all_habits(habits: List[Habit]) -> List[str]:
    """Return a list of all habit names."""
    return list(map(lambda h: h.name, habits))


def list_by_periodicity(habits: List[Habit], periodicity: str) -> List[Habit]:
    """Return all habits with the same periodicity (daily or weekly)."""
    return list(filter(lambda h: h.periodicity == periodicity, habits))


def longest_streak_for(habit: Habit) -> int:
    """Return the longest current streak for a given habit."""
    return habit.get_streak()


def longest_streak_all(habits: List[Habit]) -> Tuple[Optional[str], int]:
    """Return the habit name and value of the longest streak among all defined habits."""
    if not habits:
        return (None, 0)

    def better(a, b):
        return a if longest_streak_for(a) >= longest_streak_for(b) else b

    best_habit = reduce(better, habits)
    return (best_habit.name, longest_streak_for(best_habit))