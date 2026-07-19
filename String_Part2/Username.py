'''Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters'''

username = input("Enter Username: ")

if username[0].isalpha() :
	for i in username :
		if i.isalnum() or i == "_" :
			continue
		else :
			print("Inalid Username")
			break
	else :
		print("Valid Username")
else :
	print("Valid Username")