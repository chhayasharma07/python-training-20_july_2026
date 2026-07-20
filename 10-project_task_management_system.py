# Problem Statement: Project Task Management System (Using Python List)
# Scenario
# You have joined an IT company as a Python Developer. Your Team Lead wants a simple application to manage project tasks during development.
# Since this is the first version (Prototype), you are not allowed to use a database or files. Store all project tasks in a Python List.
# Develop a menu-driven application to manage daily project tasks.
# ________________________________________
# Functional Requirements
# Display the following menu:
# ========== Project Task Management System ==========
# 1. Add Task
# 2. View Tasks
# 3. Search Task
# 4. Update Task
# 5. Delete Task
# 6. Count Tasks
# 7. Exit
# ________________________________________
# Data Storage
# Store only the task name in a Python list.
# Example:
# tasks = []
# ________________________________________
# Operation 1 – Add Task
# Accept a task name from the user and add it to the project task list.
# Example
# Enter Task Name:
# Develop Login API

# Task added successfully.
# ________________________________________
# Operation 2 – View Tasks
# Display all available project tasks with serial numbers.
# Example
# Project Tasks

# 1 - Develop Login API
# 2 - Create Employee Dashboard
# 3 - Fix Payment Bug
# If no tasks exist:
# No tasks available.
# ________________________________________
# Operation 3 – Search Task
# Ask the user to enter a task name.
# If the task exists:
# Task Found.
# Otherwise:
# Task Not Found.
# ________________________________________
# Operation 4 – Update Task
# Display all tasks.
# Ask the user for the task number to update.
# Replace the old task with the new task.
# Example
# 1 - Develop Login API
# 2 - Create Employee Dashboard

# Enter Task Number: 2

# Enter New Task:
# Create Admin Dashboard

# Task updated successfully.
# ________________________________________
# Operation 5 – Delete Task
# Display all tasks.
# Ask the user to select the task number to delete.
# Remove the selected task.
# Example
# 1 - Develop Login API
# 2 - Create Admin Dashboard
# 3 - Fix Payment Bug

# Enter Task Number: 3

# Task deleted successfully.
# ________________________________________
# Operation 6 – Count Tasks
# Display the total number of tasks available.
# Example
# Total Project Tasks : 8
# ________________________________________
# Operation 7 – Exit
# Terminate the application.
# Thank you for using Project Task Management System.

tasks=[]

def add_task(tasks):
    task=input("Enter Task Name:")
        
    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    if len(tasks)==0:
        print("No tasks available.")
    else:
        print("Project Tasks")
        for i in range(len(tasks)):
            print(f"{i+1}-{tasks[i]}")

def search_task(tasks):
    if len(tasks)==0:
        print("No tasks available.")
    else:
        task=input("Enter Task Name:")
        if task in tasks:
            print("Task Found.")
        else:
            print("Task Not Found.")

def update_task(tasks):
    num=int(input("Enter Task Number:"))

    if num<1 or num>len(tasks):
        print("Invalid Task Number")
    else:
        new_task=input("Enter New Task:")
        tasks[num-1]=new_task
        print("Task updated successfully.")

def delete_task(tasks):
    num=int(input("Enter Task Number:"))

    if num<1 or num>len(tasks):
        print("Invalid Task Number")
    else:
        tasks.pop(num-1)
        print("Task deleted successfully.")

def count_tasks(tasks):
    print(f"Total Project Tasks : {len(tasks)}")

while True:
    print("\n========== Project Task Management System ==========")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Search Task")
    print("4.Update Task")
    print("5.Delete Task")
    print("6.Count Tasks")
    print("7.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        add_task(tasks)

    elif choice==2:
        view_tasks(tasks)

    elif choice==3:
        search_task(tasks)

    elif choice==4:
        update_task(tasks)

    elif choice==5:
        delete_task(tasks)

    elif choice==6:
        count_tasks(tasks)

    elif choice==7:
        print("Thank you for using Project Task Management System.")
        break

    else:
        print("Invalid Choice")