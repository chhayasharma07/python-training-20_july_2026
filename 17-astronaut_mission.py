# Problem Statement: Astronaut Mission Management System (Tuple + List)
# Objective
# Develop an Astronaut Mission Management System using Python Tuples and Lists. This problem is designed for intermediate-level learners to understand how immutable (tuple) and mutable (list) data structures work together in a real-world application.

# Scenario
# A space research organization wants to maintain information about astronauts participating in various space missions.
# Each astronaut's basic information should remain fixed once created, so it must be stored in a tuple.
# Each astronaut tuple should contain:
# (Astronaut ID, Astronaut Name, Space Agency, Mission List)
# The Mission List should be stored as a list because astronauts can be assigned to multiple missions during their careers.
# Example
# (201, "Neil", "NASA", ["Artemis I", "Lunar Research"])
# Where:
# Astronaut ID → Integer 
# Astronaut Name → String 
# Space Agency → String 
# Mission List → List 

# Requirements
# Create a menu-driven application that performs the following operations.

# Operation 1 – Register a New Astronaut
# Accept the following details from the user:
# Astronaut ID 
# Astronaut Name 
# Space Agency 
# Number of Missions 
# Mission Names 
# Store the astronaut information as a tuple and add it to the astronaut list.

# Operation 2 – View All Astronauts
# Display all astronaut details in a well-formatted manner.
# Example Output
# Astronaut ID : 201
# Name         : Neil
# Agency       : NASA
# Missions     : Artemis I, Lunar Research
# --------------------------------------------

# Operation 3 – Assign a New Mission
# Ask the user for:
# Astronaut ID 
# New Mission Name 
# If the astronaut exists:
# Add the new mission to the astronaut's mission list. 
# Otherwise display:
# Astronaut not found.

# Operation 4 – Complete (Remove) a Mission
# Input:
# Astronaut ID 
# Mission Name 
# If the mission exists:
# Remove it from the mission list. 
# Otherwise display an appropriate message.

# Operation 5 – Search an Astronaut
# Search using the Astronaut ID.
# Display complete astronaut information.
# If the astronaut is not available:
# Astronaut not found.

# Operation 6 – Display Experienced Astronauts
# Display only those astronauts who are currently assigned to three or more missions.
# Example Output
# Neil
# Agency : NASA
# Total Missions : 4

# Operation 7 – Display Space Agency-wise Astronaut Count
# Display how many astronauts belong to each space agency.
# Example
# NASA      : 3
# ISRO      : 2
# ESA       : 2
# SpaceX    : 1
# JAXA      : 1

# Operation 8 – Exit
# Terminate the application.

# Constraints
# Store all astronauts in a list. 
# Each astronaut record must be stored as a tuple. 
# Missions must be maintained using a list inside the tuple. 
# Do not use dictionaries. 
# Validate the Astronaut ID before performing any operation. 
# Display meaningful messages for invalid operations. 

# Sample Data
# astronauts = [
#     (201, "Neil", "NASA", ["Artemis I", "Lunar Research"]),
#     (202, "Rakesh", "ISRO", ["Gaganyaan", "Orbital Training"]),
#     (203, "Emma", "ESA", ["Mars Explorer", "Moon Base", "Deep Space Research"])
# ]

astronauts=[]

def add_astronaut(astronauts):
    astro_id=int(input("Enter Astronaut ID:"))

    for astronaut in astronauts:
        if astronaut[0]==astro_id:
            print("Astronaut ID already exists.")
            return

    astro_name=input("Enter Astronaut Name:")
    agency=input("Enter Space Agency:")

    n=int(input("Enter Number of Missions:"))
    missions=[]

    for i in range(n):
        mission=input(f"Enter Mission {i+1}:")
        missions.append(mission)

    astronaut=(astro_id,astro_name,agency,missions)

    astronauts.append(astronaut)
    print("Astronaut registered successfully.")

def view_astronauts(astronauts):
    if len(astronauts)==0:
        print("No astronauts found.")
    else:
        for astronaut in astronauts:
            print("-------------------------------------")
            print("Astronaut ID :",astronaut[0])
            print("Name :",astronaut[1])
            print("Agency :",astronaut[2])
            print("Missions :",end=" ")

            for i in range(len(astronaut[3])):
                if i==len(astronaut[3])-1:
                    print(astronaut[3][i])
                else:
                    print(astronaut[3][i],end=", ")

def assign_mission(astronauts):
    astro_id=int(input("Enter Astronaut ID:"))

    for astronaut in astronauts:
        if astronaut[0]==astro_id:
            mission=input("Enter New Mission:")

            if mission in astronaut[3]:
                print("Mission already assigned.")
            else:
                astronaut[3].append(mission)
                print("Mission assigned successfully.")
            return

    print("Astronaut not found.")

def remove_mission(astronauts):
    astro_id=int(input("Enter Astronaut ID:"))

    for astronaut in astronauts:
        if astronaut[0]==astro_id:
            mission=input("Enter Mission Name:")

            if mission in astronaut[3]:
                astronaut[3].remove(mission)
                print("Mission removed successfully.")
            else:
                print("Mission not found.")
            return

    print("Astronaut not found.")

def search_astronaut(astronauts):
    astro_id=int(input("Enter Astronaut ID:"))

    for astronaut in astronauts:
        if astronaut[0]==astro_id:
            print("Astronaut ID :",astronaut[0])
            print("Name :",astronaut[1])
            print("Agency :",astronaut[2])
            print("Missions :",astronaut[3])
            return

    print("Astronaut not found.")

def experienced_astronauts(astronauts):
    found=False

    for astronaut in astronauts:
        if len(astronaut[3])>=3:
            print("------------------------------")
            print("Name :",astronaut[1])
            print("Agency :",astronaut[2])
            print("Total Missions :",len(astronaut[3]))
            found=True

    if found==False:
        print("No experienced astronauts found.")

def agency_count(astronauts):
    if len(astronauts)==0:
        print("No astronauts found.")
    else:
        agencies=[]

        for astronaut in astronauts:
            if astronaut[2] not in agencies:
                agencies.append(astronaut[2])

        print("Agency Wise Astronaut Count")

        for agency in agencies:
            count=0

            for astronaut in astronauts:
                if astronaut[2]==agency:
                    count=count+1

            print(f"{agency} : {count}")

while True:

    print("\n========== Astronaut Mission Management System ==========")
    print("1. Register New Astronaut")
    print("2. View All Astronauts")
    print("3. Assign New Mission")
    print("4. Complete(Remove) Mission")
    print("5. Search Astronaut")
    print("6. Display Experienced Astronauts")
    print("7. Display Agency-wise Astronaut Count")
    print("8. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        add_astronaut(astronauts)

    elif choice==2:
        view_astronauts(astronauts)

    elif choice==3:
        assign_mission(astronauts)

    elif choice==4:
        remove_mission(astronauts)

    elif choice==5:
        search_astronaut(astronauts)

    elif choice==6:
        experienced_astronauts(astronauts)

    elif choice==7:
        agency_count(astronauts)

    elif choice==8:
        print("Thank you for using Astronaut Mission Management System.")
        break

    else:
        print("Invalid Choice")