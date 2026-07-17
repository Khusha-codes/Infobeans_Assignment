'''Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters'''

password = input("Enter Password: ")

digit = 0
space = 0

if password[0].isupper() and password[-1].islower() and 8<=len(password)<=15:
	for chr in password :
		if chr.isdigit() :
			digit += 1
		elif chr.isspace() :
			print("Invalid Password")
			break 
		elif chr.isalnum() :
			continue 
		else :
			space += 1

if digit >= 2 and space >= 1 :
	print("Secure Password")
else :
	print("Invalid Password")