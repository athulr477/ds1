# Student database stored as a list of dictionaries
student_db = []

# Function to add a student
def add_student(student_id, name, age, grade):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    student_db.append(student)
    print(f"Student {name} added successfully.\n")

# Function to display all students
def display_students():
    if not student_db:
        print("No student records found.\n")
        return
    print("Student Records:")
    for student in student_db:
        print(student)
    print()

# Function to search for a student by ID
def search_student(student_id):
    for student in student_db:
        if student["id"] == student_id:
            print("Student found:")
            print(student)
            return
    print("Student not found.\n")

# Function to update a student's details
def update_student(student_id, name=None, age=None, grade=None):
    for student in student_db:
        if student["id"] == student_id:
            if name:
                student["name"] = name
            if age:
                student["age"] = age
            if grade:
                student["grade"] = grade
            print(f"Student ID {student_id} updated successfully.\n")
            return
    print("Student not found.\n")

# Function to delete a student
def delete_student(student_id):
    global student_db
    student_db = [s for s in student_db if s["id"] != student_id]
    print(f"Student ID {student_id} deleted successfully.\n")
