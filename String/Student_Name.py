'''Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.'''

name = input("Enter student name:").lower()
count = 0

for i in name :
	if i not in "aeiou":
		count += 1

print("Total consonants:",count)