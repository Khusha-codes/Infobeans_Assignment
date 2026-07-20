'''Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *'''

num = input("Enter account number: ")
temp = "****"
no = len(num) - 3

if num.isdigit() :
	while no <= len(num) :
		temp += num[no-1]
		no += 1 
else :
	print("Invalid input")

print("Masked Account:",temp)