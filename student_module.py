import sqlite3

def pay_fee(student_id, amount, discount=0):
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Fee (S_Id, Amount, Discount) VALUES (?, ?, ?)", (student_id, amount, discount))
    conn.commit()
    conn.close()
    print(f"Fee payment recorded for Student ID {student_id}.")

def add_fine(student_id, amount):
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Fine (S_Id, Amount) VALUES (?, ?)", (student_id, amount))
    conn.commit()
    conn.close()
    print(f"Fine of ₹{amount} added for Student ID {student_id}.")

def view_fee(student_id):
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Fee WHERE S_Id = ?", (student_id,))
    fees = cursor.fetchall()
    conn.close()

    return fees
