appointment = {}

def book_appointment(appointment_id,patient_id,doctor_id,date,time):
	lst = [patient_id,doctor_id,date,time]
	appointment[appointment_id] = lst
	return "Appointment Book"

def display_appointment():
	for k,v in appointment.items():
		print(k,":\n",v)
	print()
