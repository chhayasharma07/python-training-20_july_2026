# Problem Statement: Office Visitor Management System (Using Python List)
# Scenario
# You are working as a Python Developer in an IT organization. The Security Department wants a simple application to maintain the list of visitors entering the office every day.
# Since this is a prototype application, do not use a database or file handling. Store all visitor names in a Python List.
# Develop a menu-driven application to manage daily visitor records.

# Functional Requirements
# Display the following menu:
# ========== Office Visitor Management System ==========
# 1. Add Visitor
# 2. View Visitors
# 3. Search Visitor
# 4. Update Visitor
# 5. Remove Visitor
# 6. Total Visitors
# 7. Exit

# Data Storage
# Store only the visitor name in a Python list.
# Example:
# visitors = []

# Operation 1 – Add Visitor
# Accept the visitor's name and add it to the visitor list.
# Example
# Enter Visitor Name:
# Enter Visitor Address:
# Enter Visitor PhoneNo:
# Enter Visitor Email:
# Enter Visitor City:

# Visitor added successfully.

# Operation 2 – View Visitors
# Display all visitors with serial numbers.
# Example
# Today's Visitors

# 1 - Rohit Sharma
# 2 - Anjali Verma
# 3 - Mohit Gupta
# If no visitors are available:
# No visitor records found.

# Operation 3 – Search Visitor
# Ask the user to enter the visitor's name.
# If found:
# Visitor Found.
# Otherwise:
# Visitor Not Found.

# Operation 4 – Update Visitor
# Display all visitors.
# Ask the user to enter the visitor number.
# Replace the existing visitor name with a new name.
# Example
# 1 - Rohit Sharma
# 2 - Anjali Verma

# Enter Visitor Number: 2

# Enter New Visitor Name:
# Neha Singh

# Visitor details updated successfully.

# Operation 5 – Remove Visitor
# Display all visitors.
# Ask the user to select the visitor number to remove.
# Delete the selected visitor from the list.
# Example
# 1 - Rohit Sharma
# 2 - Neha Singh
# 3 - Mohit Gupta

# Enter Visitor Number: 1

# Visitor removed successfully.

# Operation 6 – Total Visitors
# Display the total number of visitors currently recorded.
# Example
# Total Visitors Today : 3

# Operation 7 – Exit
# Close the application.
# Thank you for using Office Visitor Management System.

visitors=[]

def add_visitor(visitors):
    visitor_id=int(input("Enter Visitor ID:"))
    visitor_name=input("Enter Visitor Name:")
    purpose=input("Enter Purpose of Visit:")

    visitor={
    "id":visitor_id,
    "name":visitor_name,
    "purpose":purpose
    }

    visitors.append(visitor)
    print("Visitor added successfully.")

def display_visitors(visitors):
    if len(visitors)==0:
        print("No visitors found.")
    else:
        print("\nVisitor Details:")
        for i,visitor in enumerate(visitors):
            print(f"\nIndex:{i}")
            print(f"ID:{visitor['id']}")
            print(f"Name:{visitor['name']}")
            print(f"Purpose:{visitor['purpose']}")

def search_visitor(visitors):
    name=input("Enter Visitor Name:")
    found=False

    for i,visitor in enumerate(visitors):
        if visitor["name"].lower()==name.lower():
            print("\nVisitor Found")
            print(f"Index:{i}")
            print(f"ID:{visitor['id']}")
            print(f"Name:{visitor['name']}")
            print(f"Purpose:{visitor['purpose']}")
            found=True
            break

    if not found:
        print("Visitor not found.")

def update_visitor(visitors):
    name=input("Enter Visitor Name to update:")
    found=False

    for visitor in visitors:
        if visitor["name"].lower()==name.lower():
            visitor["id"]=int(input("Enter New Visitor ID:"))
            visitor["name"]=input("Enter New Visitor Name:")
            visitor["purpose"]=input("Enter New Purpose:")
            print("Visitor updated successfully.")
            found=True
            break

    if not found:
        print("Visitor not found.")

def remove_visitor(visitors):
    name=input("Enter Visitor Name to remove:")
    found=False

    for visitor in visitors:
        if visitor["name"].lower()==name.lower():
            visitors.remove(visitor)
            print("Visitor removed successfully.")
            found=True
            break

    if not found:
        print("Visitor not found.")

def total_visitors(visitors):
    print(f"Total Visitors:{len(visitors)}")

while True:
    print("\n========== Office Visitor Management System ==========")
    print("1.Add Visitor")
    print("2.View Visitors")
    print("3.Search Visitor")
    print("4.Update Visitor")
    print("5.Remove Visitor")
    print("6.Total Visitors")
    print("7.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        add_visitor(visitors)

    elif choice==2:
        display_visitors(visitors)

    elif choice==3:
        search_visitor(visitors)

    elif choice==4:
        update_visitor(visitors)

    elif choice==5:
        remove_visitor(visitors)

    elif choice==6:
        total_visitors(visitors)

    elif choice==7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")