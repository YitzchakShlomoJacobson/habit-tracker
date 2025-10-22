"""cli.py — Command-line interface for the Habit Tracker."""

import argparse
from manager import HabitManager
from fixtures import init_fixtures
import analytics as analytics_mod


def main():
    """Main CLI function to handle user commands."""
    parser = argparse.ArgumentParser(description="Habit Tracker Command Line Interface")

    parser.add_argument(
        "action",
        choices=["create", "complete", "list", "streak", "delete", "init-fixtures"],
        help="Action to perform",
    )
    parser.add_argument("--name", help="Name of the habit")
    parser.add_argument("--period", choices=["daily", "weekly"], help="Habit periodicity (daily or weekly)")
    args = parser.parse_args()

    manager = HabitManager()

    if args.action == "create":
        if not args.name or not args.period:
            print("⚠️  Please specify both --name and --period.")
            return
        manager.create_habit(args.name, args.period)
        print(f"✅ Habit created: {args.name} ({args.period})")

    elif args.action == "complete":
        if not args.name:
            print("⚠️  Please specify the habit name with --name.")
            return
        try:
            manager.complete_habit(args.name)
            print(f"✅ Habit completed: {args.name}")
        except ValueError as e:
            print(str(e))

    elif args.action == "list":
        habits = manager.list_habits()
        if not habits:
            print("📭 No habits found. Try adding one with the 'create' command.")
            return
        print("\n📋 Your Habits:")
        for h in habits:
            print(f"- {h.name} ({h.periodicity}) | Created: {h.created_at.date()} | Completions: {len(h.completions)} | Current Streak: {h.get_streak()}")

    elif args.action == "streak":
        if args.name:
            h = manager.find(args.name)
            if not h:
                print("❌ Habit not found.")
                return
            print(f"🔥 {h.name} current streak: {h.get_streak()} days/weeks")
        else:
            name, val = analytics_mod.longest_streak_all(manager.list_habits())
            if name is None:
                print("📭 No habits found.")
            else:
                print(f"🏆 Longest streak overall: {name} — {val} periods")

    elif args.action == "delete":
        if not args.name:
            print("⚠️  Please specify the habit name to delete.")
            return
        deleted = manager.delete_habit(args.name)
        if deleted:
            print(f"🗑️ Habit '{args.name}' deleted.")
        else:
            print("❌ Habit not found.")

    elif args.action == "init-fixtures":
        init_fixtures(manager)
        print("📦 Example habits loaded successfully.")


if __name__ == "__main__":
    main()