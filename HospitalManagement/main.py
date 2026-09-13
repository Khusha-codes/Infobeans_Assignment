import appointment as app
import billing as bill
import doctor as doc
import patient as pat

while True:
	print('''========== Hospital Management System ==========

1. Add Patient

2. Display Patients

3. Search Patient

4. Add Doctor

5. Display Doctors

6. Book Appointment

7. Show Appointments

8. Generate Bill

9. Exit''')

	n = int(input("Enter your choice: "))

	match n:
		case 1:
			ID = int(input("Enter Patient id: "))
			name = input("Enter Patient name: ")
			Age = int(input("Enter Patient age: "))
			gender = input("Enter Gender: ")
			disease = input("Enter Disease: ")
			mobile_no = int(input("Enter mobile number: "))
			print(pat.add_patient(ID, name, Age, gender, disease, mobile_no))

		case 2:
			print(pat.display_patients())

		case 3:
			ID = int(input("Enter Patient ID: "))
			print(pat.search_patient(ID))

		case 4:
			id = int(input("Enter Doctor id: "))
			name = input("Enter Doctor name: ")
			Specialization = input("Specialization: ")
			experience = input("Experience: ")
			fees = int("Enter Fees: ")
			print(doc.add_doctor(id, name, specialization, experience, fees))

		case 5:
			print(doc.display_doctor())

		case 6:
			appointment_id = int(input("Enter Appointment ID: "))
			patient_id = int(input("Enter Patient ID: "))
			doctor_id = int(input("Enter Doctor ID: "))
			date = input("Enter Date: ")
			time = input("Enter Time: ")
			print(app.book_appointment(appointment_id, patient_id, doctor_id, date,time))

		case 7:
			print(app.display_appointment())
		case 8:
			id = int(input("Enter Patient ID: "))
			fees = int(input("Enter Consultation Charges: "))
			cost = int(input("Medicine Cost: "))
			test = int(input("Test Charges: "))
			print(bill.generate_bill(id,fees,cost,test))

		case 9:
			print("Thanks for using Hospital Management System.")
			break
		case __:
			print("Wrong choice...! Try Again.")