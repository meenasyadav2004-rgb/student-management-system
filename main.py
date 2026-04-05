print("NEW CODE RUNNING")

from db_connection import connect_db


# ➕ ADD STUDENT
def add_student():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")

    query = "INSERT INTO students (name, age, course, email) VALUES (%s, %s, %s, %s)"
    values = (name, age, course, email)

    cursor.execute(query, values)
    conn.commit()

    print("Student added successfully!")
    conn.close()


# 📄 VIEW STUDENTS
def view_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    print("\n--- Student List ---")
    for row in data:
        print(row)

    conn.close()


# ✏️ UPDATE STUDENT
def update_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID: "))
    new_course = input("Enter new course: ")

    query = "UPDATE students SET course = %s WHERE id = %s"
    cursor.execute(query, (new_course, student_id))
    conn.commit()

    print("Updated successfully!")
    conn.close()


# ❌ DELETE STUDENT
def delete_student():
    conn = connect_db()
    cursor = conn.cursor()

    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    print("Student deleted successfully!")
    conn.close()


# 🖥️ MENU (ONLY ONE LOOP)
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice")