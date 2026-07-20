# Problem Statement: Employee Payroll Management System Using Functions in Python
# Create a menu-based Employee Payroll Management System using Python functions. The program should accept employee details, calculate salary using different payroll rules, display the salary slip, and calculate annual salary.
# Employee Details
# The program should accept:
# •	Employee ID 
# •	Employee Name 
# •	Basic Salary 
# •	Number of overtime hours 
# •	Number of leave days 

# Payroll Calculation Rules
# 1.	House Rent Allowance (HRA)
# HRA = 20% of Basic Salary 
# 2.	Dearness Allowance (DA)
# DA = 10% of Basic Salary 
# 3.	Overtime Payment
# Overtime payment = Overtime Hours × ₹500 
# 4.	Leave Deduction
# Two leave days are allowed without deduction.
# For every additional leave day, deduct ₹1,000. 
# 5.	Provident Fund Deduction (PF)
# PF = 12% of Basic Salary 
# 6.	Professional Tax 
# o	Gross Salary up to ₹30,000: ₹200 
# o	Gross Salary from ₹30,001 to ₹60,000: ₹500 
# o	Gross Salary above ₹60,000: ₹1,000 
# Salary Formulas
# Gross Salary = Basic Salary + HRA + DA + Overtime Payment

# Total Deduction = PF + Professional Tax + Leave Deduction

# Net Salary = Gross Salary - Total Deduction
# Functions to Create
# Create the following functions:
# def get_employee_details():
# Accept and return employee information.
# def calculate_hra(basic_salary):
# Calculate HRA.
# def calculate_da(basic_salary):
# Calculate DA.
# def calculate_overtime(overtime_hours):
# Calculate overtime payment.
# def calculate_leave_deduction(leave_days):
# Calculate deduction for additional leave days.
# def calculate_pf(basic_salary):
# Calculate PF deduction.
# def calculate_professional_tax(gross_salary):
# Calculate professional tax using if, elif, and else.
# def calculate_payroll(employee):
# Calculate gross salary, deductions, and net salary.
# def display_salary_slip(employee, payroll):
# Display the complete salary slip.
# Sample Salary Slip
# ----------------------------------------
#           EMPLOYEE SALARY SLIP
# ----------------------------------------
# Employee ID       : EMP101
# Employee Name     : Rahul Sharma
# Basic Salary      : ₹40,000.00
# HRA               : ₹8,000.00
# DA                : ₹4,000.00
# Overtime Payment  : ₹2,500.00
# Gross Salary      : ₹54,500.00
# PF Deduction      : ₹4,800.00
# Professional Tax  : ₹500.00
# Leave Deduction   : ₹1,000.00
# Total Deduction   : ₹6,300.00
# Net Salary        : ₹48,200.00
# ----------------------------------------
# Validation Requirements
# The program should ensure that:
# •	Employee ID and name cannot be empty. 
# •	Basic salary must be greater than zero. 
# •	Overtime hours cannot be negative. 
# •	Leave days cannot be negative. 
# •	Payroll cannot be displayed before employee details are entered. 
# •	Annual salary should be calculated as: 
# Annual Net Salary = Monthly Net Salary × 12



def get_employee_details():
   emp_id=int(input("Enter the employee id : "))
   emp_name=input("Enter your name : ")
   basic_salary=int(input("Enter the basic salary : "))
   overtime=int(input("Enter the number of overtime hours : "))
   leave=int(input("Enter the number of leave days : "))
   
   employee = {
        "emp_id": emp_id,
        "emp_name": emp_name,
        "basic_salary": basic_salary,
        "overtime": overtime,
        "leave": leave
    }

   return employee

def calculate_hra(basic_salary):
    HRA = (20* basic_salary)/100
    return HRA
    
def calculate_da(basic_salary):
     DA=(10*basic_salary)/100
     return DA
     
def calculate_overtime(overtime):
    Overtime_payment=overtime*500 
    return Overtime_payment
    
def calculate_leave_deduction(leave):
    if leave <= 2:
        return 0
    else:
        return (leave - 2) * 1000
        
def calculate_pf(basic_salary):
    PF= (12*basic_salary)/100
    return PF
    
def calculate_gross_salary(basic_salary, HRA, DA, Overtime_payment):
    gross_salary = basic_salary + HRA + DA + Overtime_payment
    return gross_salary
    
def calculate_professional_tax(gross_salary):
     if gross_salary <= 30000:
        return 200
     elif gross_salary <= 60000:
        return 500
     else:
        return 1000
    
def calculate_payroll(employee):
    basic_salary = employee["basic_salary"]

    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    overtime = calculate_overtime(employee["overtime"])

    gross_salary = calculate_gross_salary(basic_salary, hra, da, overtime)

    pf = calculate_pf(basic_salary)
    leave_deduction = calculate_leave_deduction(employee["leave"])
    professional_tax = calculate_professional_tax(gross_salary)

    total_deduction = pf + professional_tax + leave_deduction
    net_salary = gross_salary - total_deduction

    payroll = {
        "hra": hra,
        "da": da,
        "overtime": overtime,
        "gross_salary": gross_salary,
        "pf": pf,
        "professional_tax": professional_tax,
        "leave_deduction": leave_deduction,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
        "annual_salary": net_salary * 12
    }

    return payroll

def display_salary_slip(employee, payroll):
    print("\n----------------------------------------")
    print("        EMPLOYEE SALARY SLIP")
    print("----------------------------------------")

    print(f"Employee ID       : {employee['emp_id']}")
    print(f"Employee Name     : {employee['emp_name']}")
    print(f"Basic Salary      : ₹{employee['basic_salary']:.2f}")
    print(f"HRA               : ₹{payroll['hra']:.2f}")
    print(f"DA                : ₹{payroll['da']:.2f}")
    print(f"Overtime Payment  : ₹{payroll['overtime']:.2f}")
    print(f"Gross Salary      : ₹{payroll['gross_salary']:.2f}")
    print(f"PF Deduction      : ₹{payroll['pf']:.2f}")
    print(f"Professional Tax  : ₹{payroll['professional_tax']:.2f}")
    print(f"Leave Deduction   : ₹{payroll['leave_deduction']:.2f}")
    print(f"Total Deduction   : ₹{payroll['total_deduction']:.2f}")
    print(f"Net Salary        : ₹{payroll['net_salary']:.2f}")
    print(f"Annual Salary     : ₹{payroll['annual_salary']:.2f}")
    print("----------------------------------------")

employee=get_employee_details()
payroll=calculate_payroll(employee)
display_salary_slip(employee, payroll)