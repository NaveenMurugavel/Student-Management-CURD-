import student_db

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        student_db.add_student(name, age, grade)
        print("Student added successfully!")

    elif choice == '2':
        students = student_db.view_students()
        print("\n--- Students List ---")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

    elif choice == '3':
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        student_db.update_student(student_id, name, age, grade)
        print("Student updated successfully!")

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        student_db.delete_student(student_id)
        print("Student deleted successfully!")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
