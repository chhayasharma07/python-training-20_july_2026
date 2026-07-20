employee_skills=["dbms","oops","maths","html","css","java"]

def display_employee_skills(employee_skills):
    if len(employee_skills)==0:
        print("No skills found")
    else:
        print("\nEmployee Skills:")
        for i in range(len(employee_skills)):
            print(f"{i}:{employee_skills[i]}")

def update_employee_skills(employee_skills):
    index=int(input("Enter index:"))
    updated=input("Enter the updated skill:")

    if len(employee_skills)==0:
        print("No skills found")
    elif index<0 or index>=len(employee_skills):
        print("Invalid Index")
    else:
        employee_skills[index]=updated
        print("Skill updated successfully.")

def insert_employee_skills(employee_skills):
    index=int(input("Enter index:"))
    skill=input("Enter the new skill:")

    if index<0 or index>len(employee_skills):
        print("Invalid Index")
    else:
        employee_skills.insert(index,skill)
        print("Skill inserted successfully.")

def delete_employee_skills(employee_skills):
    index=int(input("Enter index:"))

    if len(employee_skills)==0:
        print("No skills found")
    elif index<0 or index>=len(employee_skills):
        print("Invalid Index")
    else:
        employee_skills.pop(index)
        print("Skill deleted successfully.")
        
def search_employee_skills(employee_skills):
    skill=input("Enter the skill to search:")
    if skill in employee_skills:
        print(f"{skill} found at index {employee_skills.index(skill)}")
    else:
        print("Skill not found")

def sort_employee_skills(employee_skills):
    employee_skills.sort()
    print("Skills sorted successfully.")

def count_employee_skills(employee_skills):
    print(f"Total number of skills:{len(employee_skills)}")
    
def display_employee_skills1(employee_skills):
    if len(employee_skills)==0:
        print("No skills found")
    else:
        print("Employee Skills : ")
        
        for index,skill in enumerate(employee_skills,start=1):
            print(f"{index}:{skill}")

while True:
    print("\n=====Employee Skills Management=====")
    print("1.Display Skills")
    print("2.Update Skill")
    print("3.Insert Skill")
    print("4.Delete Skill")
    print("5.Search Skill")
    print("6.Sort Skills")
    print("7.Count Skills")
    print("8.Exit")
    
    choice=int(input("Enter your choice:"))

    if choice==1:
      display_employee_skills1(employee_skills)

    elif choice==2:
      update_employee_skills(employee_skills)
      display_employee_skills(employee_skills)

    elif choice==3:
      insert_employee_skills(employee_skills)
      display_employee_skills(employee_skills)

    elif choice==4:
      delete_employee_skills(employee_skills)
      display_employee_skills(employee_skills)

    elif choice==5:
      search_employee_skills(employee_skills)

    elif choice==6:
      sort_employee_skills(employee_skills)
      display_employee_skills(employee_skills)

    elif choice==7:
      count_employee_skills(employee_skills)

    elif choice==8:
      print("Exiting program...")
      break

    else:
      print("Invalid choice! Please enter a number between 1 and 8.")
      

             