# Problem Statement: Cricket Team Management System (Tuple + Dictionary)
# Objective
# Develop a Cricket Team Management System using Python Tuples and Dictionaries. This intermediate-level problem helps learners understand how tuples (immutable) and dictionaries (mutable) can be combined to manage real-world data efficiently.

# Scenario
# A cricket board wants to maintain information about players participating in different tournaments.
# Each player's basic information should remain fixed once created, so it must be stored in a tuple.
# Each player tuple should contain:
# (Player ID, Player Name, Team Name, Statistics Dictionary)
# The Statistics Dictionary stores the player's performance details, which can change after every match.
# Example
# (
#     101,
#     "Virat Kohli",
#     "India",
#     {
#         "Matches": 295,
#         "Runs": 14181,
#         "Centuries": 51,
#         "HalfCenturies": 74
#     }
# )
# Where:
# Player ID → Integer 
# Player Name → String 
# Team Name → String 
# Statistics → Dictionary 

# Requirements
# Create a menu-driven application that performs the following operations.

# Operation 1 – Register a New Player
# Accept the following details:
# Player ID 
# Player Name 
# Team Name 
# Matches Played 
# Total Runs 
# Centuries 
# Half Centuries 
# Store the player information as a tuple and add it to the player list.

# Operation 2 – View All Players
# Display complete player details.
# Example Output
# Player ID      : 101
# Player Name    : Virat Kohli
# Team           : India
# Matches        : 295
# Runs           : 14181
# Centuries      : 51
# Half Centuries : 74
# ----------------------------------------

# Operation 3 – Update Player Statistics
# Ask the user for:
# Player ID 
# Allow the user to update any one of the following statistics:
# Matches 
# Runs 
# Centuries 
# Half Centuries 
# Update the value in the statistics dictionary.

# Operation 4 – Search Player
# Search using Player ID.
# Display complete player details.
# If not found:
# Player not found.

# Operation 5 – Display Highest Run Scorer
# Find and display the player who has scored the maximum runs.
# Example
# Highest Run Scorer

# Player Name : Virat Kohli
# Runs        : 14181

# Operation 6 – Display Players with More Than 10 Centuries
# Display only those players whose Centuries > 10.
# Example:
# Virat Kohli
# Centuries : 51

# Rohit Sharma
# Centuries : 34

# Operation 7 – Team-wise Player Count
# Display the number of players available in each cricket team.
# Example
# India      : 4
# Australia  : 3
# England    : 2
# Pakistan   : 1

# Operation 8 – Exit
# Terminate the application.

# Constraints
# Store all players in a list. 
# Each player must be stored as a tuple. 
# Player statistics must be maintained using a dictionary inside the tuple. 
# Do not use classes. 
# Validate Player ID before performing update or search operations. 
# Display appropriate messages for invalid inputs. 

# Sample Data
# players = [
#     (
#         101,
#         "Virat Kohli",
#         "India",
#         {
#             "Matches": 295,
#             "Runs": 14181,
#             "Centuries": 51,
#             "HalfCenturies": 74
#         }
#     ),
#     (
#         102,
#         "Joe Root",
#         "England",
#         {
#             "Matches": 180,
#             "Runs": 13500,
#             "Centuries": 36,
#             "HalfCenturies": 62
#         }
#     ),
#     (
#         103,
#         "Steve Smith",
#         "Australia",
#         {
#             "Matches": 170,
#             "Runs": 11250,
#             "Centuries": 34,
#             "HalfCenturies": 45
#         }
#     )
# ]

players=[]

def add_player(players):
    player_id=int(input("Enter Player ID:"))

    for player in players:
        if player[0]==player_id:
            print("Player ID already exists.")
            return

    player_name=input("Enter Player Name:")
    team=input("Enter Team Name:")
    matches=int(input("Enter Matches Played:"))
    runs=int(input("Enter Total Runs:"))
    centuries=int(input("Enter Centuries:"))
    half_centuries=int(input("Enter Half Centuries:"))

    statistics={
        "Matches":matches,
        "Runs":runs,
        "Centuries":centuries,
        "HalfCenturies":half_centuries
    }

    player=(player_id,player_name,team,statistics)

    players.append(player)
    print("Player added successfully.")

def view_players(players):
    if len(players)==0:
        print("No players found.")
    else:
        for player in players:
            print("----------------------------------")
            print("Player ID :",player[0])
            print("Player Name :",player[1])
            print("Team :",player[2])
            print("Matches :",player[3]["Matches"])
            print("Runs :",player[3]["Runs"])
            print("Centuries :",player[3]["Centuries"])
            print("Half Centuries :",player[3]["HalfCenturies"])

def update_statistics(players):
    player_id=int(input("Enter Player ID:"))

    for player in players:
        if player[0]==player_id:

            print("1. Matches")
            print("2. Runs")
            print("3. Centuries")
            print("4. Half Centuries")

            choice=int(input("Enter Choice:"))

            if choice==1:
                player[3]["Matches"]=int(input("Enter New Matches:"))
                print("Statistics updated successfully.")

            elif choice==2:
                player[3]["Runs"]=int(input("Enter New Runs:"))
                print("Statistics updated successfully.")

            elif choice==3:
                player[3]["Centuries"]=int(input("Enter New Centuries:"))
                print("Statistics updated successfully.")

            elif choice==4:
                player[3]["HalfCenturies"]=int(input("Enter New Half Centuries:"))
                print("Statistics updated successfully.")

            else:
                print("Invalid Choice")

            return

    print("Player not found.")

def search_player(players):
    player_id=int(input("Enter Player ID:"))

    for player in players:
        if player[0]==player_id:
            print("Player ID :",player[0])
            print("Player Name :",player[1])
            print("Team :",player[2])
            print("Matches :",player[3]["Matches"])
            print("Runs :",player[3]["Runs"])
            print("Centuries :",player[3]["Centuries"])
            print("Half Centuries :",player[3]["HalfCenturies"])
            return

    print("Player not found.")

def highest_run_scorer(players):
    if len(players)==0:
        print("No players found.")
    else:
        highest=players[0]

        for player in players:
            if player[3]["Runs"]>highest[3]["Runs"]:
                highest=player

        print("Highest Run Scorer")
        print("Player Name :",highest[1])
        print("Runs :",highest[3]["Runs"])

def players_centuries(players):
    found=False

    for player in players:
        if player[3]["Centuries"]>10:
            print("----------------------")
            print("Player Name :",player[1])
            print("Centuries :",player[3]["Centuries"])
            found=True

    if found==False:
        print("No player has more than 10 centuries.")

def team_count(players):
    if len(players)==0:
        print("No players found.")
    else:
        teams=[]

        for player in players:
            if player[2] not in teams:
                teams.append(player[2])

        print("Team Wise Player Count")

        for team in teams:
            count=0

            for player in players:
                if player[2]==team:
                    count=count+1

            print(f"{team} : {count}")

while True:

    print("\n========== Cricket Team Management System ==========")
    print("1. Register New Player")
    print("2. View All Players")
    print("3. Update Player Statistics")
    print("4. Search Player")
    print("5. Display Highest Run Scorer")
    print("6. Display Players with More Than 10 Centuries")
    print("7. Team-wise Player Count")
    print("8. Exit")

    choice=int(input("Enter Choice:"))

    if choice==1:
        add_player(players)

    elif choice==2:
        view_players(players)

    elif choice==3:
        update_statistics(players)

    elif choice==4:
        search_player(players)

    elif choice==5:
        highest_run_scorer(players)

    elif choice==6:
        players_centuries(players)

    elif choice==7:
        team_count(players)

    elif choice==8:
        print("Thank you for using Cricket Team Management System.")
        break

    else:
        print("Invalid Choice")