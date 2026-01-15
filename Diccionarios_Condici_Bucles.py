# Jonathan Villamizar
# DAM 2

# Diccionarios, condicionales y bucles.

# Main dictionary where students will be stored
students = {}


# Create student

students["xavi"] = {
    "age": 20,
    "course": "DAM2",
    "languages": {"Python", "Java"},
    "grade": 7.5
}

students["bianca"] = {
    "age": 22,
    "course": "DAW1",
    "languages": {"HTML", "CSS", "JavaScript"},
    "grade": 6.2
}

students["alfredo"] = {
    "age": 21,
    "course": "DAM1",
    "languages": {"Python", "C++"},
    "grade": 9.1
}


# Function to show students
def show_students():
    print("\nSTUDENT LIST")
    for name, data in students.items():
        print(f"\nStudent: {name.capitalize()}")
        print(f"Age: {data['age']}")
        print(f"Course: {data['course']}")
        print(f"Languages: {', '.join(data['languages'])}")
        print(f"Average grade: {data['grade']}")

        # Grade conditionals
        grade = data["grade"]
        if grade < 5:
            status = "Fail"
        elif grade < 7:
            status = "Pass"
        elif grade < 9:
            status = "Good"
        else:
            status = "Excellent"

        print(f"Final assessment: {status}")


# Filter students
def filter_students():
    print("\nFILTERED STUDENTS (age > 18 and grade >= 7)")
    for name, data in students.items():
        if data["age"] > 18 and data["grade"] >= 7:
            print(f"- {name.capitalize()} ({data['grade']})")


# Search student
def find_student():
    name = input("Enter the student's name: ").lower()

    if name in students:
        data = students[name]
        print(f"\nStudent found: {name.capitalize()}")
        print(f"Age: {data['age']}")
        print(f"Course: {data['course']}")
        print(f"Languages: {', '.join(data['languages'])}")
        print(f"Average grade: {data['grade']}")
    else:
        print("Student not found.")


# Add student
def add_student():
    print("\nAdd new student")
    name = input("Name (or 'exit' to cancel): ").lower()

    # Use of early return
    if name == "exit":
        print("Cancelling registration...")
        return

    age = int(input("Age: "))
    course = input("Course: ")
    languages = input("Languages (separated by commas): ")
    grade = float(input("Average grade: "))

    # Convert languages to set
    languages_set = {l.strip() for l in languages.split(",")}

    students[name] = {
        "age": age,
        "course": course,
        "languages": languages_set,
        "grade": grade
    }

    print(f"Student {name.capitalize()} added successfully.")


# Average of grades
def average_grades():
    if len(students) == 0:
        print("There are no registered students.")
        return

    total = sum(data["grade"] for data in students.values())
    average = total / len(students)
    print(f"\nThe average grade of all students is: {average:.2f}")


# Menu with while
while True:
    print("\nMAIN MENU")
    print("1. Show students")
    print("2. Search student")
    print("3. Add student")
    print("4. Filter students")
    print("5. Average of grades")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        show_students()
    elif option == "2":
        find_student()
    elif option == "3":
        add_student()
    elif option == "4":
        filter_students()
    elif option == "5":
        average_grades()
    elif option == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Try again.")