'''Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only'''

id = input("Enter ID: ")

if id[0:3] == "EMP" and len(id) == 8 and id[3::].isdigit() :
	print("Valid Employee ID")
else :
	print("Invalid Employee ID")