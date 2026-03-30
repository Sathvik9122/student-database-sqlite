import sqlite3

def connect_db():
    return sqlite3.connect("Student.db")

def create_table():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                s_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)

def get_department():
    departments = {
        1: "CSE",
        2: "ME",
        3: "EEE",
        4: "Civil",
        5: "BBA",
        6: "MBA"
    }

    while True:
        print("\nSelect Department:")
        for key, value in departments.items():
            print(f"{key}. {value}")

        try:
            choice = int(input("Enter choice (1-6): "))
            if choice in departments:
                return departments[choice]
            else:
                print(" Invalid choice. Try again.")
        except ValueError:
            print(" Please enter a number.")

def add_student():
    name = input("Enter Name: ").strip()
    department = get_department()

    try:
        year = int(input("Enter Birth Year: "))
    except ValueError:
        print(" Invalid year.")
        return

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, department, year) VALUES (?, ?, ?)",
            (name, department, year)
        )
    print(" Student added successfully!")

def view_students():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()

        if not rows:
            print("No records found.")
        else:
            print("\n--- Student Records ---")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}, Year: {row[3]}")

def update_student():
    s_id = int(input("Enter Student ID to update: "))
    new_name = input("Enter new name: ")

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE students SET name=? WHERE s_id=?", (new_name, s_id))
        print("Updated successfully!")
def delete_student():
    try:
        s_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE s_id = ?", (s_id,))
        
        if cur.rowcount == 0:
            print("No student found with that ID.")
        else:
            print("Student deleted successfully!")

def main():
    create_table()

    while True:
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Value")
        print("4. Delete Student")
        print("5.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
