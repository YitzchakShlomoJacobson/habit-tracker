# 🧩 Habit Tracker Backend

A simple **Python backend** for tracking and analyzing daily and weekly habits.

Users can:
- Create new habits
- Mark completions
- See current streaks
- Analyze longest streaks
- Load 5 predefined example habits (fixtures)

---

## ⚙️ Installation

### Requirements
- Python **3.7 or higher**
- pip (Python package manager)

### Steps

Open your terminal (or VS Code terminal) and run:

```bash
cd Desktop/Object-Oriented-and-Functional-Programming-project-legit

# Create a virtual environment
python -m venv venv

# Activate it
# 🪟 Windows:
venv\Scripts\activate
# 🍎 macOS / 🐧 Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
▶️ Usage
1️⃣ Load example habits
bash
python cli.py init-fixtures
2️⃣ List your habits
bash
python cli.py list
3️⃣ Create a new habit
bash
python cli.py create --name "Workout" --period daily
4️⃣ Complete a habit
bash
python cli.py complete --name "Workout"
5️⃣ View longest streak
bash
python cli.py streak
🧪 Run Tests
bash
pytest
This runs the automated test suite to verify everything works correctly.

🧠 Technologies Used
Python 3.7+

SQLite3 for storage

argparse for CLI

pytest for testing

OOP + Functional Programming

📦 Folder Structure
pgsql
Object-Oriented-and-Functional-Programming-project-legit/
│
├── habit.py
├── storage.py
├── manager.py
├── analytics.py
├── fixtures.py
├── cli.py
├── requirements.txt
├── README.md
└── tests/
    └── test_habit.py
✨ Developed with care — simple, clean, and extensible.