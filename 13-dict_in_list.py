students=[]

def add_student(students):
    college=input("Enter College Name : ").upper()
    student_id=int(input("Enter Student ID:"))

    for student in students:
        if student["college"]==college and student["id"]==student_id:
            print("Student ID already exists in this college.")
            return

    student_name=input("Enter Student Name:")
    age=int(input("Enter Age:"))
    branch=input("Enter Branch:")

    student={
        "college":college,
        "id":student_id,
        "name":student_name,
        "age":age,
        "branch":branch
    }

    students.append(student)
    print("Student added successfully.")

def view_students(students):
    if len(students)==0:
        print("No student records found.")
    else:
        for student in students:
            print("----------------------------")
            print("College :",student["college"])
            print("ID      :",student["id"])
            print("Name    :",student["name"])
            print("Age     :",student["age"])
            print("Branch  :",student["branch"])

def search_student(students):
    college=input("Enter College Name : ").upper()
    student_id=int(input("Enter Student ID:"))

    for student in students:
        if student["college"]==college and student["id"]==student_id:
            print("Student Found")
            print(student)
            return

    print("Student Not Found.")

def update_student(students):
    college=input("Enter College Name (MRI/MRU): ").upper()
    student_id=int(input("Enter Student ID:"))

    for student in students:
        if student["college"]==college and student["id"]==student_id:
            student["name"]=input("Enter New Name:")
            student["age"]=int(input("Enter New Age:"))
            student["branch"]=input("Enter New Branch:")
            print("Student updated successfully.")
            return

    print("Student Not Found.")

def delete_student(students):
    college=input("Enter College Name:").upper()
    student_id=int(input("Enter Student ID:"))

    for student in students:
        if student["college"]==college and student["id"]==student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student Not Found.")

def count_students(students):
    print("Total Students :",len(students))


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        add_student(students)

    elif choice==2:
        view_students(students)

    elif choice==3:
        search_student(students)

    elif choice==4:
        update_student(students)

    elif choice==5:
        delete_student(students)

    elif choice==6:
        count_students(students)

    elif choice==7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")