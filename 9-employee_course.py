employee=[{"id":1,"name":"A","designation":"Developer"},{"id":2,"name":"B","designation":"Tester"},{"id":3,"name":"C","designation":"Manager"}]

def add_employee(employee):
    index=int(input("Enter index:"))

    emp_id=input("Enter Employee ID:")
    if emp_id.strip()=="":
        print("Employee ID cannot be empty")
        return

    emp_id=int(emp_id)

    emp_name=input("Enter Employee Name:")
    if emp_name.strip()=="":
        print("Employee Name cannot be empty")
        return

    designation=input("Enter Employee Designation:")
    if designation.strip()=="":
        print("Designation cannot be empty")
        return

    new_employee={"id":emp_id,"name":emp_name,"designation":designation}

    if index<0 or index>len(employee):
        print("Invalid Index")
    else:
        employee.insert(index,new_employee)
        print("Employee added successfully.")
        
def display_employee(employee):
    if len(employee)==0:
        print("No employee found")
    else:
        print("\nEmployee :")
        for i in range(len(employee)):
            print(f"{i}:{employee[i]}")
            
def search_employee(employee):
    empl=input("Enter the employee to search:")
    if empl in employee:
        print(f"{empl} found at index {employee.index(empl)}")
    else:
        print("Employee not found")

while True:
    print("\n=====Employee Skills Management=====")
    print("1.Add Employee")
    print("2.View Employee")
    print("3.Search Employe")
    print("4.Exit")
    
    choice=int(input("Enter your choice:"))

    if choice==1:
      add_employee(employee)
      display_employee(employee)

    elif choice==2:
      display_employee(employee)

    elif choice==3:
      search_employee(employee)

    elif choice==4:
      print("Exiting program...")
      break

    else:
      print("Invalid choice! Please enter a number between 1 and 4.")