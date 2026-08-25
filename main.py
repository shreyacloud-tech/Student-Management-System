import json  
FILE_NAME="students.json"
students=[]
def add_students():
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Please enter a valid student ID")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists")
            return

    name = input("Enter student name: ")

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Please enter a valid age")
        return

    course = input("Enter student course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students()
    print("Student added successfully")
def view_students():
    if students==[]:
        print("No students found")
    else:
        for student in students:
            print("Student id:",student["id"])
            print("name:",student["name"])
            print("age:",student["age"])
            print("course:",student["course"])
def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))
    except ValueError:
        print("Please enter a valid student ID")
        return

    found = False

    for student in students:
        if student["id"] == student_id:
            print("Student id:", student["id"])
            print("name:", student["name"])
            print("age:", student["age"])
            print("course:", student["course"])
            found = True
            break

    if not found:
        print("Student not found")
def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Please enter a valid student ID ")
        return
    found=False
    for student in students:
        if student["id"]==student_id:
            new_name=input("Enter new name:")
            try:
                new_age=int(input("Enter new age:"))
            except ValueError:
                print("Please enter a valid age")
                return
            new_course=input("Enter new course:")
            student["name"]=new_name
            student["age"]=new_age
            student["course"]=new_course
            save_students()
            print("Student updated successfully")
            found=True
            break
    if not found:
        print("Student not found")
def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    found=False
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            save_students()
            print("Student deleted successfully")
            found=True
            break
    if not found:
        print("Student not found")
def save_students():
    with open(FILE_NAME, "w") as file: 
        json.dump(students, file, indent=4)
def load_students():
    global students

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
load_students()
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("please enter a number from 1 to 6.")
        continue
    if choice==1:
        add_students()
    elif choice==2:
        view_students()
    elif choice==3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
    elif choice==6:
        print("Thank you for using student management system!")
        break
    else:
        print("Invalid choice. Please Try again")