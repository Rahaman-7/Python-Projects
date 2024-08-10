students_grade = {}

def add(name,grade):
    students_grade[name] = grade
    print(f"the {name} and {grade} is added successfully")


def update(name,grade):
    if name in students_grade:
        students_grade[name] = grade
        print(f"{name} and {grade} is updated successfully")
    else:
        print(f"{name} is not found")
    

def delete(name):
    if name in students_grade:
        del students_grade[name]
        print(f"{name} is deleted successfully")
    else:
        print(f"{name} is not found")

def view():
    if students_grade:
        for name,grade in students_grade.items():
            print(f"{name}:{grade}")
    else:
        print("no students found/added")


def main():
    while True:
        print("------------------------------------------")
        print("Welcome To Student Grade Management system")
        print("------------------------------------------")
        print("1.add\n2.update\n3.delete\n4.view\n5.exit")

        choice = int(input("enter your choice: "))
        if choice == 1:
            name = input("enter the name of student: ")
            grade = int(input("enter the grade of student: "))
            add(name,grade)
        elif choice == 2:
            name = input("enter the name of student: ")
            grade = int(input("enter the grade of student: "))
            update(name,grade)
        elif choice == 3:
            name = input("enter the student name: ")
            delete(name)
        elif choice == 4:
            view()
        elif choice == 5:
            print("closing student grade mangement system")
            break
        else:
            print("invalid choice")

main()

