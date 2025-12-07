# Quiz System (Python Tkinter + SQLite)

A simple **Quiz Management System** built with **Python**, **Tkinter**, and **SQLite**.
Supports **Admin** panel for creating quizzes & questions and **User** panel for taking quizzes.

---

## 🎮 Features

**Admin Panel:**

* Create quizzes
* Add multiple-choice questions (A/B/C/D)
* Simple and intuitive GUI

**User Panel:**

* View available quizzes
* Take quizzes with multiple-choice questions
* Instant scoring after completion

**Database:**

* SQLite (`quiz.db`) stores quizzes and questions
* Easy to extend and modify

---

## 💻 Technologies Used

* Python 3
* Tkinter (GUI)
* SQLite (Database)

---

## 📂 Project Structure

```
.
├── quiz_database.py    # SQLite DB handling functions
├── quiz_gui.py         # Tkinter GUI for Admin & User
├── main.py             # Entry point; initializes DB and GUI
├── quiz.db             # SQLite database file
└── README.md           # This file
```

---

## 🚀 How to Run

1. Make sure Python 3.x is installed.
2. Clone or download the repository:

```bash
git clone https://github.com/your-username/quiz-system.git
```

3. Navigate to the project folder:

```bash
cd quiz-system
```

4. Run the program:

```bash
python main.py
```

> `main.py` will automatically create the SQLite database (`quiz.db`) and necessary tables if they don’t exist.

---

## 🎯 Controls

**Admin Panel:**

* Create Quiz: Enter quiz title
* Add Question: Enter Quiz ID, question text, options A–D, and correct answer

**User Panel:**

* Select a quiz from the list
* Answer multiple-choice questions
* View final score

---

## 🧩 Code Overview

* `quiz_database.py` – Handles all database operations (create tables, add quizzes/questions, retrieve data)
* `quiz_gui.py` – GUI using Tkinter for Admin and User functionality
* `main.py` – Initializes the database and launches the GUI
* `quiz.db` – SQLite database storing all quizzes and questions

---

## 📌 Future Improvements

* User authentication system
* Save high scores
* Timer for quizzes
* Export/import quizzes (JSON/CSV)
* Improved UI design

---

## 📄 License

This project is open-source and free to use for learning or personal projects.


