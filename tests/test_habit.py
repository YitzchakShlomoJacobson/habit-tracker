"""tests/test_habit.py — Unit tests for the Habit class streak logic."""

from habit import Habit
from datetime import datetime, timedelta


def test_daily_streak_continuous():
    """Test that a daily habit streak is counted correctly when days are consecutive."""
    h = Habit("Exercise", "daily")
    today = datetime.now().date()
    for i in range(5):
        h.complete(datetime.combine(today - timedelta(days=i), datetime.min.time()))
    assert h.get_streak() == 5


def test_daily_streak_broken():
    """Test that streak breaks when a day is missed."""
    h = Habit("Read", "daily")
    today = datetime.now().date()
    h.complete(datetime.combine(today - timedelta(days=1), datetime.min.time()))
    # missed today
    assert h.get_streak() == 0


def test_weekly_streak():
    """Test that weekly streaks are counted properly."""
    h = Habit("Call Mom", "weekly")
    now = datetime.now()
    h.complete(now)
    h.complete(now - timedelta(weeks=1))
    h.complete(now - timedelta(weeks=2))
    assert h.get_streak() >= 3