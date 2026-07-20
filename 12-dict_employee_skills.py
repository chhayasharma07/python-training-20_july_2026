employee={}

def add_employee_skill(employee):
    emp_name=input("Enter Employee Name:")
    skill=input("Enter Employee Skill:")
    employee[emp_name]=skill
    print("Employee skill added successfully.")

def view_employee(employee):
    if len(employee)==0:
        print("No employee found.")
    else:
        print("\nEmployee Details:")
        for name,skill in employee.items():
            print(f"Name:{name}")
            print(f"Skill:{skill}")
            print("------------------")

def search_employee_skill(employee):
    emp_name=input("Enter Employee Name:")
    if emp_name in employee:
        print(f"Employee Name:{emp_name}")
        print(f"Skill:{employee[emp_name]}")
    else:
        print("Employee not found.")

while True:
    print("\n=====Employee Skills Management System=====")
    print("1.Add Employee Skill")
    print("2.View All Employees")
    print("3.Search Employee Skill")
    print("4.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        add_employee_skill(employee)

    elif choice==2:
        view_employee(employee)

    elif choice==3:
        search_employee_skill(employee)

    elif choice==4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")