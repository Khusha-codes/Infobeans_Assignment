from Manager.List import Record
from Module.Classes import (
    Patient,
    GeneralPatient,
    EmergencyPatient,
    CorporatePatient,
    InsurancePatient,)

L = Record()

def loop_1st() :
    print("""
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. View Patient Bill
4. Exit
""")
    choice = int(input("Enter Choice: "))
    return choice

def loop_2nd():
    print("""
========================================
       CHOOSE CATEGORY
========================================

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient
""")
    choice = int(input("Enter Choice: "))
    return choice

def main_call() :
  while True :
    m = loop_1st()
    match m:
        case 1:
            id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            n = loop_2nd()

            match n:

                case 1:
                    obj = GeneralPatient()
                    obj.id = id
                    obj.name = name
                    obj.age = age
                    obj.day = int(input("Enter Number of Days: "))
                    obj.M_Charge = int(input("Enter Medicine Charge: "))
                    obj.display()
                    L.add(obj)
                    break

                case 2:
                    obj = EmergencyPatient()
                    obj.id = id
                    obj.name = name
                    obj.age = age
                    obj.day = int(input("Enter Number of Days: "))
                    obj.M_Charge = int(input("Enter Medicine Charge: "))
                    obj.display()
                    L.add(obj)
                    break

                case 3:
                    obj = InsurancePatient()
                    obj.id = id
                    obj.name = name
                    obj.age = age
                    obj.day = int(input("Enter Number of Days: "))
                    obj.M_Charge = int(input("Enter Medicine Charge: "))
                    obj.display()
                    L.add(obj)
                    break

                case 4:
                    obj = CorporatePatient()
                    obj.id = id
                    obj.name = name
                    obj.age = age
                    obj.day = int(input("Enter Number of Days: "))
                    obj.M_Charge = int(input("Enter Medicine Charge: "))
                    obj.display()
                    L.add(obj)
                    break

                case 5:
                    print("Please Enter Valid Entery")

        case 2:
            id = input("Enter Patient ID: ")
            obj = L.find(id)
            if obj:
                obj.display
            else:
                print("Patient record not found.")

        case 3:
            print("Thank you for using Hospital Management System.")
            break

        case 4:
            print("Try Again")