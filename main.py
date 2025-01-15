import tkinter as tk
from tkinter import messagebox
from admin_module import add_student, view_students
from student_module import pay_fee, add_fine, view_fee

def add_student_ui():
    def submit():
        first_name = entry_fname.get()
        last_name = entry_lname.get()
        program = entry_program.get()

        if first_name and last_name and program:
            add_student(first_name, last_name, program)
            messagebox.showinfo("Success", "Student added successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    window = tk.Toplevel(root)
    window.title("Add Student")

    tk.Label(window, text="First Name").pack()
    entry_fname = tk.Entry(window)
    entry_fname.pack()

    tk.Label(window, text="Last Name").pack()
    entry_lname = tk.Entry(window)
    entry_lname.pack()

    tk.Label(window, text="Program").pack()
    entry_program = tk.Entry(window)
    entry_program.pack()

    tk.Button(window, text="Submit", command=submit).pack()

def view_students_ui():
    students = view_students()
    details = "\n".join([f"ID: {s[0]}, Name: {s[1]} {s[2]}, Program: {s[3]}" for s in students])
    if not details:
        details = "No students found."
    messagebox.showinfo("Student Details", details)

def pay_fee_ui():
    def submit():
        student_id = entry_sid.get()
        amount = entry_amount.get()

        if student_id.isdigit() and amount.isdigit():
            pay_fee(int(student_id), float(amount))
            messagebox.showinfo("Success", "Fee payment recorded.")
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid input!")

    window = tk.Toplevel(root)
    window.title("Pay Fee")

    tk.Label(window, text="Student ID").pack()
    entry_sid = tk.Entry(window)
    entry_sid.pack()

    tk.Label(window, text="Amount").pack()
    entry_amount = tk.Entry(window)
    entry_amount.pack()

    tk.Button(window, text="Submit", command=submit).pack()

root = tk.Tk()
root.title("Fee Management System")

tk.Button(root, text="Add Student", command=add_student_ui).pack(pady=5)
tk.Button(root, text="View Students", command=view_students_ui).pack(pady=5)
tk.Button(root, text="Pay Fee", command=pay_fee_ui).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
