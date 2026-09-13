doctor = {}

def add_doctor(id,name,specialization,experience,fees):
	lst = [name,specialization,experience,fees]
	doctor[id] = lst
	return "Doctor's record had added"

def display_doctor():
	for k,v in doctor.items():
		print(k,":\n",v)
	print()
	