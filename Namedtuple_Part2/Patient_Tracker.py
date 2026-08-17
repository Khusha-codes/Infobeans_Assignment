'''A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.'''

from collections import namedtuple
patient = nametuple("ptt",["patient_id","patient_name","age","disease"])

n = int(input("Enter number of student: "))
patients = []

for i in range(n):
	print("Enter details")
	id = int(input("Patient ID: "))
	n = input("Patient Name: ")
	age = int(input("Enter Age: "))
	d = input("Enter disease")
	s = patient(id,n,age,d)
	patients.append(s)
print()

for i in patients:
	print(*i)
print()

print("Patient with age above 60 years:")
for i in patients:
	if i.age > 60 :
		print(i.name)
print()

d = input("Enter disease: ")
count = 0
for i in students:
	if i.desease == d:
		count += 1
print(count,"Number of Patients suffering from",d)
print("")


