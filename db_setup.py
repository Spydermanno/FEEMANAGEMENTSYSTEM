import sqlite3

def setup_database():
    conn = sqlite3.connect("fee_management.db")
    cursor = conn.cursor()

    # Create Admin Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Admin (
        Ad_Id INTEGER PRIMARY KEY,
        Password TEXT NOT NULL
    )""")

    # Create Student Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        S_Id INTEGER PRIMARY KEY,
        F_Name TEXT NOT NULL,
        L_Name TEXT NOT NULL,
        Program TEXT NOT NULL
    )""")

    # Create Fee Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fee (
        F_Id INTEGER PRIMARY KEY,
        S_Id INTEGER NOT NULL,
        Amount REAL NOT NULL,
        Discount REAL DEFAULT 0,
        FOREIGN KEY (S_Id) REFERENCES Student(S_Id)
    )""")

    # Create Fine Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fine (
        Tb_Id INTEGER PRIMARY KEY,
        S_Id INTEGER NOT NULL,
        Amount REAL NOT NULL,
        FOREIGN KEY (S_Id) REFERENCES Student(S_Id)
    )""")

    # Insert Default Admin
    cursor.execute("INSERT OR IGNORE INTO Admin (Ad_Id, Password) VALUES (1, 'admin123')")

    conn.commit()
    conn.close()
    print("Database setup completed.")

# Run the setup
if __name__ == "__main__":
    setup_database()
