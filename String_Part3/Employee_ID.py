'''Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase'''

name = input("Enter employee name: ")
id = name[0].upper()

for i in range(len(name)) :
	if name[i-1] == " " and name[i].isalpha() :
		id += name[i].upper()

print("Employee Short ID:",id)