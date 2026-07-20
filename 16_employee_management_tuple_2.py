# Problem Statement: Employee Project Management System (Tuple + List)
# Objective
# Design and develop an Employee Project Management System using Python Tuples and Lists. The objective is to understand how immutable data (tuples) can be combined with mutable data (lists) to build a real-world application.

# Scenario
# A software company wants to maintain information about employees and the projects assigned to them.
# Each employee's information should be stored in a tuple because employee details should not be modified accidentally.
# Each employee tuple should contain:
# (Employee ID, Employee Name, Department, Project List)
# The Project List should be a list because projects can be assigned, removed, or updated over time.
# Example:
# (101, "Rahul", "AI", ["Chatbot", "Resume Analyzer"])
# Here,
# Employee ID → Integer 
# Employee Name → String 
# Department → String 
# Project List → List 

# Requirements
# Create a menu-driven program that performs the following operations.
# Operation 1 – Add Employee
# Allow the user to enter:
# Employee ID 
# Employee Name 
# Department 
# Number of Projects 
# Project Names 
# Store the employee as a tuple and add it to the employee list.

# Operation 2 – View All Employees
# Display all employee details in a formatted manner.
# Example Output
# Employee ID : 101
# Name        : Rahul
# Department  : AI
# Projects    : Chatbot, Resume Analyzer
# ---------------------------------------

# Operation 3 – Assign a New Project
# Ask the user for:
# Employee ID 
# New Project Name 
# If the employee exists,
# Append the project to the employee's project list. 
# Otherwise display
# Employee not found.

# Operation 4 – Remove a Project
# Input:
# Employee ID 
# Project Name 
# If the project exists,
# Remove it from the project list.
# Otherwise display an appropriate message.

# Operation 5 – Search Employee
# Search using Employee ID.
# Display complete employee details.
# If not found,
# Employee not found.

# Operation 6 – Display Employees Working on Multiple Projects
# Display only those employees who are working on more than two projects.
# Example
# Rahul
# Projects : 4

# Operation 7 – Display Department-wise Employee Count
# Calculate and display the number of employees in each department.
# Example
# AI       : 3
# Python   : 2
# Cloud    : 4
# Testing  : 1

# Operation 8 – Exit
# Terminate the program.

# Constraints
# Store all employees in a list. 
# Each employee must be stored as a tuple. 
# The project information must be maintained using a list inside the tuple. 
# Do not use dictionaries. 
# Validate Employee ID before performing operations. 
# Display meaningful messages for invalid inputs. 

# Sample Data
# employees = [
#     (101, "Rahul", "AI", ["Chatbot", "Resume Analyzer"]),
#     (102, "Priya", "Cloud", ["Azure Migration"]),
#     (103, "Amit", "Python", ["Payroll System", "Inventory", "Billing"])
# ]

employees=[]

def add_employee(employees):
    emp_id=int(input("Enter Employee ID:"))

    for employee in employees:
        if employee[0]==emp_id:
            print("Employee ID already exists.")
            return

    emp_name=input("Enter Employee Name:")
    department=input("Enter Department:")

    n=int(input("Enter Number of Projects:"))
    projects=[]

    for i in range(n):
        project=input(f"Enter Project {i+1}:")
        projects.append(project)

    employee=(emp_id,emp_name,department,projects)

    employees.append(employee)
    print("Employee added successfully.")

def view_employee(employees):
    if len(employees)==0:
        print("No employees found.")
    else:
        for employee in employees:
            print("--------------------------------")
            print("Employee ID :",employee[0])
            print("Name :",employee[1])
            print("Department :",employee[2])
            print("Projects :",end=" ")

            for i in range(len(employee[3])):
                if i==len(employee[3])-1:
                    print(employee[3][i])
                else:
                    print(employee[3][i],end=", ")

def assign_project(employees):
    emp_id=int(input("Enter Employee ID:"))

    for employee in employees:
        if employee[0]==emp_id:
            project=input("Enter New Project:")

            if project in employee[3]:
                print("Project already assigned.")
            else:
                employee[3].append(project)
                print("Project assigned successfully.")
            return

    print("Employee not found.")

def remove_project(employees):
    emp_id=int(input("Enter Employee ID:"))

    for employee in employees:
        if employee[0]==emp_id:
            project=input("Enter Project Name:")

            if project in employee[3]:
                employee[3].remove(project)
                print("Project removed successfully.")
            else:
                print("Project not found.")
            return

    print("Employee not found.")

def search_employee(employees):
    emp_id=int(input("Enter Employee ID:"))

    for employee in employees:
        if employee[0]==emp_id:
            print("Employee ID :",employee[0])
            print("Name :",employee[1])
            print("Department :",employee[2])
            print("Projects :",employee[3])
            return

    print("Employee not found.")

def multiple_projects(employees):
    found=False

    for employee in employees:
        if len(employee[3])>2:
            print("--------------------------")
            print("Name :",employee[1])
            print("Projects :",len(employee[3]))
            found=True

    if found==False:
        print("No employee is working on more than two projects.")

def department_count(employees):
    if len(employees)==0:
        print("No employees found.")
    else:
        departments=[]

        for employee in employees:
            if employee[2] not in departments:
                departments.append(employee[2])

        print("Department Wise Employee Count")

        for dept in departments:
            count=0

            for employee in employees:
                if employee[2]==dept:
                    count=count+1

            print(f"{dept} : {count}")

while True:

    print("\n========== Employee Project Management System ==========")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Assign New Project")
    print("4. Remove Project")
    print("5. Search Employee")
    print("6. Display Employees Working on Multiple Projects")
    print("7. Display Department-wise Employee Count")
    print("8. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        add_employee(employees)

    elif choice==2:
        view_employee(employees)

    elif choice==3:
        assign_project(employees)

    elif choice==4:
        remove_project(employees)

    elif choice==5:
        search_employee(employees)

    elif choice==6:
        multiple_projects(employees)

    elif choice==7:
        department_count(employees)

    elif choice==8:
        print("Thank you for using Employee Project Management System.")
        break

    else:
        print("Invalid Choice")