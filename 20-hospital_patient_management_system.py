# Problem Statement: Hospital Patient Management System
# Dictionary Containing a List of Dictionaries
# Objective
# Develop a Hospital Patient Management System using Python, where each patient is represented by a dictionary and the patient’s medical visits are stored as a list of dictionaries inside the patient dictionary.
# This intermediate-level problem will help learners practise nested data structures, searching, updating, calculation, filtering, and menu-driven programming.
# Scenario
# A hospital wants to maintain patient details and their medical visit history.
# Each patient dictionary should contain:
# {
#     "PatientId": 101,
#     "PatientName": "Aman Verma",
#     "Age": 35,
#     "City": "Noida",
#     "Visits": [
#         {
#             "VisitId": 1,
#             "DoctorName": "Dr. Mehta",
#             "Department": "Cardiology",
#             "ConsultationFee": 1200,
#             "MedicinesCost": 800,
#             "Status": "Completed"
#         },
#         {
#             "VisitId": 2,
#             "DoctorName": "Dr. Sharma",
#             "Department": "General Medicine",
#             "ConsultationFee": 700,
#             "MedicinesCost": 500,
#             "Status": "Pending"
#         }
#     ]
# }
# Multiple patients should be stored in a list:
# patients = []
# Functional Requirements
# Create a menu-driven Python program with the following operations.
# 1. Add a New Patient
# Accept:
# Patient ID 
# Patient Name 
# Age 
# City 
# The patient should initially have an empty Visits list.
# Do not allow duplicate Patient IDs.
# 2. Add a Medical Visit
# Ask for the Patient ID.
# If the patient exists, accept:
# Visit ID 
# Doctor Name 
# Department 
# Consultation Fee 
# Medicines Cost 
# Visit Status 
# Create a visit dictionary and add it to the patient’s Visits list.
# Do not allow duplicate Visit IDs for the same patient.
# 3. View All Patients
# Display every patient along with their complete visit history.
# Example:
# Patient ID   : 101
# Patient Name : Aman Verma
# Age          : 35
# City         : Noida

# Visit ID          : 1
# Doctor Name       : Dr. Mehta
# Department        : Cardiology
# Consultation Fee  : 1200
# Medicines Cost    : 800
# Status            : Completed
# ----------------------------------------
# 4. Search Patient by ID
# Ask the user for a Patient ID.
# Display:
# Patient details 
# Total number of visits 
# Complete visit history 
# Display Patient not found when the ID does not exist.
# 5. Update Visit Status
# Accept:
# Patient ID 
# Visit ID 
# New Status 
# Allowed statuses may include:
# Scheduled
# Pending
# Completed
# Cancelled
# Update the Status field of the matching visit.
# 6. Calculate Total Medical Bill
# Ask for the Patient ID.
# For every visit, calculate:
# Visit Bill = Consultation Fee + Medicines Cost
# Then calculate the total medical bill for the patient.
# Example:
# Visit 1 Bill : ₹2000
# Visit 2 Bill : ₹1200
# -----------------------
# Total Bill   : ₹3200
# 7. Display Patients with Multiple Visits
# Display patients who have more than two medical visits.
# Show:
# Patient ID 
# Patient Name 
# Number of Visits 
# 8. Display Department-wise Visit Count
# Count the total number of visits for each hospital department.
# Example:
# Cardiology       : 3
# General Medicine : 5
# Orthopaedics     : 2
# Neurology        : 1
# Do not use another permanent dictionary for storage. The count may be calculated during program execution.
# 9. Find the Patient with the Highest Medical Bill
# Calculate the total bill of every patient and display the patient whose total medical expenses are the highest.
# Example:
# Patient with Highest Medical Bill

# Patient ID   : 101
# Patient Name : Aman Verma
# Total Bill   : ₹8500
# 10. Remove a Visit Record
# Accept:
# Patient ID 
# Visit ID 
# Remove the matching visit dictionary from the patient’s Visits list.
# Display appropriate messages when the patient or visit is not found.
# 11. Exit
# Terminate the program.
# Constraints
# Store all patients in a list. 
# Store every patient as a dictionary. 
# Store visit records as a list of dictionaries inside the patient dictionary. 
# Do not use classes. 
# Patient ID must be unique. 
# Visit ID must be unique for each patient. 
# Age must be greater than zero. 
# Consultation fee and medicine cost cannot be negative. 
# Display meaningful validation messages. 
# Sample Data
# patients = [
#     {
#         "PatientId": 101,
#         "PatientName": "Aman Verma",
#         "Age": 35,
#         "City": "Noida",
#         "Visits": [
#             {
#                 "VisitId": 1,
#                 "DoctorName": "Dr. Mehta",
#                 "Department": "Cardiology",
#                 "ConsultationFee": 1200,
#                 "MedicinesCost": 800,
#                 "Status": "Completed"
#             },
#             {
#                 "VisitId": 2,
#                 "DoctorName": "Dr. Sharma",
#                 "Department": "General Medicine",
#                 "ConsultationFee": 700,
#                 "MedicinesCost": 500,
#                 "Status": "Pending"
#             }
#         ]
#     },
#     {
#         "PatientId": 102,
#         "PatientName": "Riya Singh",
#         "Age": 28,
#         "City": "Delhi",
#         "Visits": [
#             {
#                 "VisitId": 1,
#                 "DoctorName": "Dr. Kapoor",
#                 "Department": "Orthopaedics",
#                 "ConsultationFee": 1000,
#                 "MedicinesCost": 650,
#                 "Status": "Completed"
#             }
#         ]
#     }
# ]

patients=[]

def add_patient(patients):

    patient_id=int(input("Enter Patient ID:"))

    for patient in patients:
        if patient["PatientId"]==patient_id:
            print("Patient ID already exists.")
            return

    patient_name=input("Enter Patient Name:")
    age=int(input("Enter Age:"))

    if age<=0:
        print("Age must be greater than zero.")
        return

    city=input("Enter City:")

    patient={
        "PatientId":patient_id,
        "PatientName":patient_name,
        "Age":age,
        "City":city,
        "Visits":[]
    }

    patients.append(patient)
    print("Patient added successfully.")


def add_visit(patients):

    patient_id=int(input("Enter Patient ID:"))

    for patient in patients:

        if patient["PatientId"]==patient_id:

            visit_id=int(input("Enter Visit ID:"))

            for visit in patient["Visits"]:
                if visit["VisitId"]==visit_id:
                    print("Visit ID already exists.")
                    return

            doctor=input("Enter Doctor Name:")
            department=input("Enter Department:")

            consultation_fee=int(input("Enter Consultation Fee:"))
            if consultation_fee<0:
                print("Consultation Fee cannot be negative.")
                return

            medicine_cost=int(input("Enter Medicines Cost:"))
            if medicine_cost<0:
                print("Medicines Cost cannot be negative.")
                return

            status=input("Enter Status:")

            visit={
                "VisitId":visit_id,
                "DoctorName":doctor,
                "Department":department,
                "ConsultationFee":consultation_fee,
                "MedicinesCost":medicine_cost,
                "Status":status
            }

            patient["Visits"].append(visit)

            print("Visit added successfully.")
            return

    print("Patient not found.")


def view_patients(patients):

    if len(patients)==0:
        print("No patients found.")

    else:

        for patient in patients:

            print("---------------------------------------")
            print("Patient ID :",patient["PatientId"])
            print("Patient Name :",patient["PatientName"])
            print("Age :",patient["Age"])
            print("City :",patient["City"])

            print("\nVisits")

            if len(patient["Visits"])==0:
                print("No Visits")

            else:

                for visit in patient["Visits"]:

                    print("Visit ID :",visit["VisitId"])
                    print("Doctor Name :",visit["DoctorName"])
                    print("Department :",visit["Department"])
                    print("Consultation Fee :",visit["ConsultationFee"])
                    print("Medicines Cost :",visit["MedicinesCost"])
                    print("Status :",visit["Status"])
                    print()


def search_patient(patients):

    patient_id=int(input("Enter Patient ID:"))

    for patient in patients:

        if patient["PatientId"]==patient_id:

            print("Patient ID :",patient["PatientId"])
            print("Patient Name :",patient["PatientName"])
            print("Age :",patient["Age"])
            print("City :",patient["City"])
            print("Total Visits :",len(patient["Visits"]))

            print("\nVisits")

            if len(patient["Visits"])==0:
                print("No Visits")

            else:

                for visit in patient["Visits"]:

                    print("Visit ID :",visit["VisitId"])
                    print("Doctor Name :",visit["DoctorName"])
                    print("Department :",visit["Department"])
                    print("Consultation Fee :",visit["ConsultationFee"])
                    print("Medicines Cost :",visit["MedicinesCost"])
                    print("Status :",visit["Status"])
                    print()

            return

    print("Patient not found.")
    
def update_visit_status(patients):

    patient_id=int(input("Enter Patient ID:"))

    for patient in patients:

        if patient["PatientId"]==patient_id:

            visit_id=int(input("Enter Visit ID:"))

            for visit in patient["Visits"]:

                if visit["VisitId"]==visit_id:

                    print("1. Scheduled")
                    print("2. Pending")
                    print("3. Completed")
                    print("4. Cancelled")

                    choice=int(input("Enter Choice:"))

                    if choice==1:
                        visit["Status"]="Scheduled"

                    elif choice==2:
                        visit["Status"]="Pending"

                    elif choice==3:
                        visit["Status"]="Completed"

                    elif choice==4:
                        visit["Status"]="Cancelled"

                    else:
                        print("Invalid Choice")
                        return

                    print("Visit status updated successfully.")
                    return

            print("Visit not found.")
            return

    print("Patient not found.")


def total_bill(patients):

    patient_id=int(input("Enter Patient ID:"))

    for patient in patients:

        if patient["PatientId"]==patient_id:

            total=0

            for visit in patient["Visits"]:

                bill=visit["ConsultationFee"]+visit["MedicinesCost"]

                print(f'Visit {visit["VisitId"]} Bill : {bill}')

                total=total+bill

            print("---------------------------")
            print("Total Bill :",total)
            return

    print("Patient not found.")


def multiple_visits(patients):

    found=False

    for patient in patients:

        if len(patient["Visits"])>2:

            print("---------------------------")
            print("Patient ID :",patient["PatientId"])
            print("Patient Name :",patient["PatientName"])
            print("Number of Visits :",len(patient["Visits"]))

            found=True

    if found==False:
        print("No patient has more than two visits.")


def department_count(patients):

    if len(patients)==0:
        print("No patients found.")
        return

    departments=[]

    for patient in patients:

        for visit in patient["Visits"]:

            if visit["Department"] not in departments:
                departments.append(visit["Department"])

    print("Department Wise Visit Count")

    for dept in departments:

        count=0

        for patient in patients:

            for visit in patient["Visits"]:

                if visit["Department"]==dept:
                    count=count+1

        print(f"{dept} : {count}")