'''1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit'''

print("Menu\n")
print('''=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit\n''')

while True :
	Patient = {
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}

	n = int(input("Enter your choice: "))

	match n:
		case 1:
			name = input("Enter name: ")
			age = int(input("Enter age: "))
			gen = input("Enter gender: ")
			dis = input("Enter disease: ")
			doc = input("Enter doctor: ")
			id = int(input("Enter Patient ID: "))
			Patient[id] = {"name":name,"age":age,"gender":gen,"disease":dis,"doctor":doc}

		case 2:
			id = int(input("Enter Patient ID: "))
			for k,v in Patient[id].items():
				print(k," : ",v)
		case 3:
			id = int(input("Enter Patient ID: "))
			dis = input("Enter new disease: ")
			Patient[id]["disease"] = dis
		case 4:
			id = int(input("Enter Patient ID: "))
			del Patient[id]
		case 5:
			for key,value in Patient.items():
				print("--------------------------------")
				for k,v in value.items():
					print(k," : ",v)
				print("--------------------------------")
		case 6:
			count = 0
			for i in Patient:
				count += 1
			print("Total Patients :",count)
		case 7:
			dis = input("Enter disease: ")
			for k,v in Patient.items():
				if Patient[k]["disease"] == dis:
					print(k," : ",Patient[k]["name"])
		case 8:
			print("Oldest Patient Details")
			m = 0
			for k,v in Patient.items():
				if m < Patient[k]["age"]:
					m = k
			for k,v in Patient[m].items():
				print(k," : ",v)
		case 9:
			print("Youngest Patient Details")
			m = 0
			for k,v in Patient.items():
				if m > Patient[k]["age"]:
					m = k
			for k,v in Patient[m].items():
				print(k," : ",v)
		case 10:
			print("Thank you")
			break