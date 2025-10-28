# 🧩 Habit Tracker Backend (Python Project)

A clean, modular **Python backend** for tracking and analyzing daily and weekly habits.  
Built using **Object-Oriented Programming (OOP)** and **Functional Programming (FP)** principles.

---

## 🌟 Key Features

- ✅ Create and manage daily or weekly habits  
- ✅ Track completions (“check-offs”) and streaks  
- ✅ Analyze performance with pure functional analytics  
- ✅ Persist data using **SQLite3**  
- ✅ Access everything from a simple **Command Line Interface (CLI)**  
- ✅ Includes 5 predefined habits and 4 weeks of example tracking data  
- ✅ Comprehensive unit tests with **pytest**

---

## ⚙️ Installation Guide

### 🧰 Requirements
- Python **3.7+**
- pip package manager
- (optional) Virtual environment tool (`venv` or `conda`)

### 🧩 Setup Instructions

**1️⃣ Clone the repository**
git clone https://github.com/YitzchakShlomoJacobson/habit-tracker.git
cd habit-tracker

cpp

**2️⃣ Create and activate a virtual environment**
python -m venv venv
venv\Scripts\activate # Windows

or
source venv/bin/activate # macOS/Linux

markdown

**3️⃣ Install dependencies**
pip install -r requirements.txt

yaml

---

## ▶️ Usage Instructions

**Initialize predefined example habits**
python cli.py init-fixtures

css

**List all habits**
python cli.py list

sql

**Create a new habit**
python cli.py create --name "Workout" --period daily

css

**Mark a habit as completed**
python cli.py complete --name "Workout"

sql

**View the longest streak across all habits**
python cli.py streak

yaml

---

## 🧪 Run Unit Tests
Make sure everything works correctly:
pytest

yaml
All tests are located in the `tests/` directory and validate habit logic, streak calculation, and data persistence.

---

## 🧠 Design & Architecture

This project combines **Object-Oriented** and **Functional** programming principles.

### 🏗️ Object-Oriented Components
- **Habit** – represents a single habit and its completion events  
- **HabitManager** – manages multiple habits and coordinates persistence  
- **Storage** – handles SQLite database operations  

### 🧮 Functional Components
Analytics functions follow the functional paradigm:
- `list_all_habits()`
- `list_by_periodicity()`
- `longest_streak_for()`
- `longest_streak_all()`

---

## 🗂️ Folder Structure

habit-tracker/
│
├── analytics.py # FP analytics module
├── cli.py # Command-line interface
├── fixtures.py # Predefined sample data
├── habit.py # Core Habit class
├── manager.py # Habit management logic
├── storage.py # SQLite persistence
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── tests/
└── test_habit.py # Unit tests

yaml

---

## 💡 Technologies Used

- Python 3.7+
- SQLite3
- argparse
- pytest
- Functional Programming (FP)
- Object-Oriented Programming (OOP)

---

## 🏁 Project Summary

This Habit Tracker backend demonstrates robust software engineering principles:
- Reliable tracking of habits and streaks  
- Clean, modular, and extensible design  
- Analytics powered by pure functional programming  
- Tested and verified with pytest

---

## 👨‍💻 Author

**Yitzchak Shlomo Jacobson**  
📧 *yitzchak-shlomo.jacobson@iu-study.org*  
🗓️ *2025*  
📍 Built for IU Object-Oriented & Functional Programming Portfolio Project
