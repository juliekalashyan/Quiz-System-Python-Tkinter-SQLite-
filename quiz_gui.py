import tkinter as tk
from tkinter import messagebox
from quiz_database import add_quiz, add_question, get_quizzes, get_questions


def admin_window():
    win = tk.Toplevel()
    win.title("Admin Panel")
    win.geometry("350x250")
    win.configure(bg="#f0f8ff")

    tk.Label(win, text="Admin Panel", font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=20)

    tk.Button(win, text="Create Quiz", width=25, bg="#4caf50", fg="white",
              font=("Arial", 12), command=create_quiz_window).pack(pady=10)

    tk.Button(win, text="Add Question to Quiz", width=25, bg="#2196f3", fg="white",
              font=("Arial", 12), command=add_question_window).pack(pady=10)


def create_quiz_window():
    win = tk.Toplevel()
    win.title("Create Quiz")
    win.geometry("450x200")
    win.configure(bg="#f0f8ff")

    tk.Label(win, text="Quiz Title:", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=10)
    title_entry = tk.Entry(win, width=50, font=("Arial", 14))
    title_entry.pack()

    def create_quiz():
        title = title_entry.get().strip()
        if not title:
            messagebox.showerror("Error", "Title is required")
            return
        add_quiz(title)
        messagebox.showinfo("Success", f"Quiz '{title}' created!")
        title_entry.delete(0, tk.END)

    tk.Button(win, text="Create Quiz", command=create_quiz, bg="#4caf50", fg="white",
              font=("Arial", 14, "bold")).pack(pady=15)


def add_question_window():
    win = tk.Toplevel()
    win.title("Add Question")
    win.geometry("550x450")
    win.configure(bg="#f0f8ff")

    tk.Label(win, text="Quiz ID:", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(anchor="w", pady=3)
    quiz_id_entry = tk.Entry(win, width=10, font=("Arial", 14))
    quiz_id_entry.pack(anchor="w", pady=3)

    tk.Label(win, text="Question Text:", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(anchor="w", pady=3)
    question_entry = tk.Entry(win, width=50, font=("Arial", 14))
    question_entry.pack(anchor="w", pady=3)

    tk.Label(win, text="Option A:", font=("Arial", 14), bg="#f0f8ff").pack(anchor="w", pady=2)
    a_entry = tk.Entry(win, width=50, font=("Arial", 14))
    a_entry.pack(anchor="w", pady=2)

    tk.Label(win, text="Option B:", font=("Arial", 14), bg="#f0f8ff").pack(anchor="w", pady=2)
    b_entry = tk.Entry(win, width=50, font=("Arial", 14))
    b_entry.pack(anchor="w", pady=2)

    tk.Label(win, text="Option C:", font=("Arial", 14), bg="#f0f8ff").pack(anchor="w", pady=2)
    c_entry = tk.Entry(win, width=50, font=("Arial", 14))
    c_entry.pack(anchor="w", pady=2)

    tk.Label(win, text="Option D:", font=("Arial", 14), bg="#f0f8ff").pack(anchor="w", pady=2)
    d_entry = tk.Entry(win, width=50, font=("Arial", 14))
    d_entry.pack(anchor="w", pady=2)

    tk.Label(win, text="Correct Answer (A/B/C/D):", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(anchor="w", pady=5)
    correct_entry = tk.Entry(win, width=10, font=("Arial", 14))
    correct_entry.pack(anchor="w", pady=5)

    def add_q():
        try:
            quiz_id = int(quiz_id_entry.get())
        except:
            messagebox.showerror("Error", "Quiz ID must be a number")
            return

        if quiz_id not in [q[0] for q in get_quizzes()]:
            messagebox.showerror("Error", "Quiz ID does not exist")
            return

        text = question_entry.get().strip()
        a = a_entry.get().strip()
        b = b_entry.get().strip()
        c = c_entry.get().strip()
        d = d_entry.get().strip()
        correct = correct_entry.get().strip().upper()

        if correct not in ["A", "B", "C", "D"]:
            messagebox.showerror("Error", "Correct answer must be A, B, C, or D")
            return

        add_question(quiz_id, text, a, b, c, d, correct)
        messagebox.showinfo("Success", "Question added!")

        question_entry.delete(0, tk.END)
        a_entry.delete(0, tk.END)
        b_entry.delete(0, tk.END)
        c_entry.delete(0, tk.END)
        d_entry.delete(0, tk.END)
        correct_entry.delete(0, tk.END)

    tk.Button(win, text="Add Question", command=add_q, bg="#2196f3", fg="white",
              font=("Arial", 14, "bold")).pack(pady=15)



def user_window():
    win = tk.Toplevel()
    win.title("Take Quiz")
    win.geometry("550x500")
    win.configure(bg="#fffaf0")

    quizzes = get_quizzes()
    if not quizzes:
        tk.Label(win, text="No quizzes available", font=("Arial", 14, "italic"), bg="#fffaf0").pack(pady=20)
        return

    tk.Label(win, text="Choose a Quiz:", font=("Arial", 14, "bold"), bg="#fffaf0").pack(pady=10)
    quiz_list = tk.Listbox(win, width=50, height=6, font=("Arial", 12))
    for q in quizzes:
        quiz_list.insert(tk.END, f"{q[0]} - {q[1]}")
    quiz_list.pack(pady=5)

    def start_quiz():
        selection = quiz_list.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a quiz")
            return

        quiz_id = quizzes[selection[0]][0]
        questions = get_questions(quiz_id)
        if not questions:
            messagebox.showinfo("Info", "This quiz has no questions yet")
            return

        for w in win.winfo_children():
            w.destroy()

        score = 0
        index = 0

        frame = tk.Frame(win, bg="#fffaf0")
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        def show_question():
            nonlocal score, index
            for w in frame.winfo_children():
                w.destroy()

            q = questions[index]
            tk.Label(frame, text=f"Q{index+1}: {q[1]}", font=("Arial", 14, "bold"),
                     bg="#fffaf0", wraplength=500, justify="left").pack(pady=5)

            answer_var = tk.StringVar()
            options = [
                ("A. " + q[2], "A"),
                ("B. " + q[3], "B"),
                ("C. " + q[4], "C"),
                ("D. " + q[5], "D")
            ]
            for text, val in options:
                tk.Radiobutton(frame, text=text, variable=answer_var, value=val,
                               bg="#fffaf0", font=("Arial", 12), anchor="w").pack(fill="x", pady=2)

            def submit_answer():
                nonlocal score, index
                if answer_var.get() == q[6]:
                    score += 1
                index += 1
                if index < len(questions):
                    show_question()
                else:
                    for w in win.winfo_children():
                        w.destroy()
                    tk.Label(win,text="Quiz Finished!", font=("Arial", 18, "bold"), 
                             bg="#fffaf0", fg="#2f855a").pack(pady=(40, 5))

                    tk.Label(win, text=f"Score: {score}/{len(questions)}", font=("Arial", 20, "bold"), 
                        bg="#fffaf0", fg="#e38d33").pack(pady=(0, 40))

                    tk.Button(win, text="Close", command=win.destroy,
                              bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=10)

            tk.Button(frame, text="Next", command=submit_answer,
                      bg="#4caf50", fg="white", font=("Arial", 12)).pack(pady=10)

        show_question()

    tk.Button(win, text="Start Quiz", command=start_quiz,
              bg="#2196f3", fg="white", font=("Arial", 12)).pack(pady=10)



def main_gui():
    root = tk.Tk()
    root.title("Quiz System")
    root.geometry("450x350")
    root.configure(bg="#e6e6fa")

    tk.Label(root, text="Quiz System", font=("Comic Sans MS", 24, "bold"), bg="#e6e6fa").pack(pady=30)
    tk.Button(root, text="Admin", width=25, command=admin_window,
              bg="#4caf50", fg="white", font=("Arial", 12)).pack(pady=15)
    tk.Button(root, text="User", width=25, command=user_window,
              bg="#2196f3", fg="white", font=("Arial", 12)).pack(pady=15)

    root.mainloop()

