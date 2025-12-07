import sqlite3

DB_NAME = "quiz.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
    );
    """)

    conn.commit()
    conn.close()

def add_quiz(title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO quizzes (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def add_question(quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO questions (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (quiz_id, question_text, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()
    conn.close()

def get_quizzes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM quizzes")
    data = cur.fetchall()
    conn.close()
    return data

def get_questions(quiz_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, question_text, option_a, option_b, option_c, option_d, correct_answer
        FROM questions WHERE quiz_id = ?
    """, (quiz_id,))
    data = cur.fetchall()
    conn.close()
    return data
