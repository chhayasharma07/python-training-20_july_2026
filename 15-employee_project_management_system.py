# Problem Statement: Employee Project Management System (Tuple + List) 
# Objective
# Develop a Python menu-driven application to manage employee project information using Tuples and Lists.
# •	Use a tuple to store employee details (immutable data). 
# •	Inside the tuple, use a list to store the projects assigned to that employee (mutable data). 
# This problem helps learners understand that while tuples cannot be modified, they can contain mutable objects like lists, whose contents can be updated.
# ________________________________________
# Data Structure
# Store each employee in the following format:
# (
#     Employee_ID,
#     Employee_Name,
#     Department,
#     [Project_List]
# )
# Example
# employee = (
#     101,
#     "Gaurav Joshi",
#     "AI Developer",
#     ["Payroll System", "HR Portal"]
# )
# ________________________________________
# Menu Operations
# 1. View Employee Details
# Display:
# •	Employee ID 
# •	Employee Name 
# •	Department 
# •	Assigned Projects 
# ________________________________________
# 2. Add New Project
# Ask the user for a project name and add it to the employee's project list.
# Example:
# Enter Project Name:
# AI Recruitment System
# Output:
# Project added successfully.
# ________________________________________
# 3. Remove a Project
# Allow the user to remove a project from the list.
# Example:
# Enter Project Name:
# HR Portal
# Output:
# Project removed successfully.
# If the project does not exist:
# Project not found.
# ________________________________________
# 4. Search a Project
# Ask the user for a project name.
# Display whether the employee is working on that project.
# Example:
# Enter Project Name:
# Payroll System
# Output:
# Project Assigned.
# Otherwise
# Project Not Assigned.
# ________________________________________
# 5. Display Total Number of Projects
# Count the projects assigned to the employee.
# Example Output
# Total Projects : 4
# ________________________________________
# 6. Display Projects Alphabetically
# Sort and display the project list without changing the employee tuple.
# Example Output
# AI Recruitment
# Attendance System
# Payroll System
# Website Portal
# ________________________________________
# 7. Exit
# Terminate the application.

employee=(
    101,
    "Chhaya Sharma",
    "CSE",
    ["Payroll System","HR Portal"]
)

def view_employee(employee):
    print("Employee ID :",employee[0])
    print("Employee Name :",employee[1])
    print("Department :",employee[2])
    print("Projects :")
    for i in range(len(employee[3])):
        print(f"{i+1}-{employee[3][i]}")

def add_project(employee):
    project=input("Enter Project Name:")

    if project in employee[3]:
        print("Project already assigned.")
    else:
        employee[3].append(project)
        print("Project added successfully.")

def remove_project(employee):
    project=input("Enter Project Name:")

    if project in employee[3]:
        employee[3].remove(project)
        print("Project removed successfully.")
    else:
        print("Project not found.")

def search_project(employee):
    project=input("Enter Project Name:")

    if project in employee[3]:
        print("Project Assigned.")
    else:
        print("Project Not Assigned.")

def count_projects(employee):
    print("Total Projects :",len(employee[3]))

def sort_projects(employee):
    if len(employee[3])==0:
        print("No projects assigned.")
    else:
        temp=sorted(employee[3])
        print("Projects in Alphabetical Order")
        for i in range(len(temp)):
            print(f"{i+1}-{temp[i]}")

while True:

    print("\n========== Employee Project Management System ==========")
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove Project")
    print("4. Search Project")
    print("5. Display Total Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        view_employee(employee)

    elif choice==2:
        add_project(employee)

    elif choice==3:
        remove_project(employee)

    elif choice==4:
        search_project(employee)

    elif choice==5:
        count_projects(employee)

    elif choice==6:
        sort_projects(employee)

    elif choice==7:
        print("Thank you for using Employee Project Management System.")
        break

    else:
        print("Invalid Choice")
