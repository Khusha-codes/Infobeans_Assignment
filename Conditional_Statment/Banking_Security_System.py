'''A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password'''

name = input("Enter username: ")
password = input("Enter password: ")

if name == "admin":
	print("Valid user.")
	if len(password) >= 8 :
		print("Strong Password.")
else :
	print("Invalid username.")