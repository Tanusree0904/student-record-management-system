import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    marks INTEGER
)
""")
conn.commit()


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, branch, marks)
        )
        conn.commit()
        print("Student record added successfully.\n")
    except sqlite3.IntegrityError:
        print("Error: Roll number already exists.\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for r in records:
        print(f"Roll: {r[0]}, Name: {r[1]}, Branch: {r[2]}, Marks: {r[3]}")
    print()


def search_student():
    roll = input("Enter Roll Number to search: ")
    cursor.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    record = cursor.fetchone()

    if record:
        print(f"Roll: {record[0]}, Name: {record[1]}, Branch: {record[2]}, Marks: {record[3]}\n")
    else:
        print("Student record not found.\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    cursor.execute("DELETE FROM students WHERE roll = ?", (roll,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student record deleted successfully.\n")
    else:
        print("Student record not found.\n")


while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program.")
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.\n")