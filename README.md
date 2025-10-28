🧩 Habit Tracker Backend (Python Project)

A clean, modular Python backend for tracking and analyzing daily and weekly habits.
Built using Object-Oriented Programming (OOP) and Functional Programming (FP) principles.

🌟 Key Features

✅ Create and manage daily or weekly habits
✅ Track completions (“check-offs”) and streaks
✅ Analyze performance with pure functional analytics
✅ Persist data using SQLite3
✅ Access everything from a simple Command Line Interface (CLI)
✅ Includes 5 predefined habits and 4 weeks of example tracking data
✅ Comprehensive unit tests with pytest

⚙️ Installation Guide
🧰 Requirements

Python 3.7+

pip package manager

(optional) Virtual environment tool such as venv or conda

🧩 Setup Instructions

1️⃣ Clone the repository

git clone https://github.com/YitzchakShlomoJacobson/habit-tracker.git
cd habit-tracker


2️⃣ Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux


3️⃣ Install dependencies

pip install -r requirements.txt

▶️ Usage Instructions
Initialize predefined example habits
python cli.py init-fixtures

List all habits
python cli.py list

Create a new habit
python cli.py create --name "Workout" --period daily

Mark a habit as completed
python cli.py complete --name "Workout"

View the longest streak across all habits
python cli.py streak

🧪 Running Unit Tests

Ensure everything works correctly:

pytest


All tests are located in the tests/ directory and validate habit logic, streak calculation, and data persistence.

🧠 Design & Architecture

This project combines Object-Oriented and Functional programming principles:

🏗️ Object-Oriented Components

Habit Class: represents a single habit, its periodicity, and completion events.

HabitManager: manages multiple habits, integrates storage and CLI interactions.

Storage: provides persistent data handling with SQLite3.

🧮 Functional Components

Analytics functions are written in a functional style:

list_all_habits()

list_by_periodicity()

longest_streak_for()

longest_streak_all()

🗂️ Folder Structure
habit-tracker/
│
├── analytics.py        # FP analytics module
├── cli.py              # Command-line interface
├── fixtures.py         # Predefined sample data
├── habit.py            # Core Habit class
├── manager.py          # Habit management logic
├── storage.py          # SQLite3 persistence
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── tests/
    └── test_habit.py   # Unit tests

💡 Technologies Used

Python 3.7+

SQLite3

argparse

pytest

Functional Programming (FP)

Object-Oriented Programming (OOP)

🏁 Project Summary

This Habit Tracker backend was developed to demonstrate strong programming structure and modular design.
It fulfills all project acceptance criteria, providing:

Reliable tracking of habits and streaks

Clean and maintainable codebase

Analytical insights using functional programming

👨‍💻 Author

Yitzchak Shlomo Jacobson
📧 yitzchak-shlomo.jacobson@iu-study.org

🗓️ 2025
📍 Built for IU Object-Oriented & Functional Programming Portfolio Project