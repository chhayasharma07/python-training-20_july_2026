employees=("A","B","C")

def display_employee(employees):
    if len(employees)==0:
        print("No employees found.")
    else:
        print("Employee List")
        for i in range(len(employees)):
            print(f"{i+1}-{employees[i]}")

def search_employee(employees):
    if len(employees)==0:
        print("No employees found")
    else:
        emp=input("Enter Employee Name:")
        if emp in employees:
            print("Employee Found")
        else:
            print("Employee Not Found")

def insert_employee(employees):
    emp=input("Enter Employee Name:")
    index=int(input("Enter Position:"))

    temp=list(employees)

    if index<1 or index>len(temp)+1:
        print("Invalid Position")
    else:
        temp.insert(index-1,emp)
        employees=tuple(temp)
        print("Employee inserted successfully.")

    return employees

while True:
    print("\n===== Employee Management System =====")
    print("1.Display Employees")
    print("2.Search Employee")
    print("3.Insert Employee")
    print("4.Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        display_employee(employees)

    elif choice==2:
        search_employee(employees)

    elif choice==3:
        employees=insert_employee(employees)

    elif choice==4:
        print("EXIT")
        break

    else:
        print("Invalid Choice")