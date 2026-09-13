patient = {}

def add_patient(ID,name,Age,gender,disease,mobile_no):
	lst = [name,Age,gender,disease,mobile_no]
	patient[id] = lst
	return "Patient Detail Update"

def display_patients():
	for k,v in patient.items():
		print(k,":\n",v)

def search_patient(ID):
	if ID in patient:
		return (patient[ID])
	else:
		return "Patient not found"
