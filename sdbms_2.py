students = {}
while True:
    print("\n--- Student Database Menu ---")
    print("1. Add student")
    print("2. Update student")
    print("3. Remove student")
    print("4. View all students")
    print("5. Search student")
    print("6. Show total number of students")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        roll = int(input("Enter roll number :: "))
        name = input("Enter name :: ")
        students[roll] = name
        print(f"Student Added :: {roll} : {name}")

    elif choice == '2':
        roll = int(input("Enter roll number :: "))
        if roll in students:
            name = input("Enter name :: ")
            students[roll] = name
            print(f"Student Updated :: {roll} : {name}")
        else:
            print("Roll number not found.")

    elif choice == '3':
        roll = int(input("Enter roll number :: "))
        if roll in students:
            removed = students.pop(roll)
            print(f"Removed Student :: {roll} : {name}")
        else:
            print("Roll number not found")

    elif choice == '4':
        if students:
            print("All student: ")
            for roll, name in students.items():
                print(f"Roll :: {roll}, Name :: {name}")
        else:
            print("No structure in databse")

    elif choice == '5':
        roll = int(input("Enter roll number :: "))
        if roll in students:
            print(f"Found :: {roll} : {name}")
        else:
            print("Roll number not found")

    elif choice == '6':
        print(f"Total Students :: {len(students)}")

    elif choice == '7':
        print("Thank you !!")
        break

    else:
        print("Invalid Choice ! ")
        break