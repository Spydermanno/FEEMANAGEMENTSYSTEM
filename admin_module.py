import sqlite3

def add_student(first_name, last_name, program):
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Student (F_Name, L_Name, Program) VALUES (?, ?, ?)", (first_name, last_name, program))
    conn.commit()
    conn.close()
    print(f"Student {first_name} {last_name} added successfully!")

def view_students():
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Student")
    students = cursor.fetchall()
    conn.close()

    return students
