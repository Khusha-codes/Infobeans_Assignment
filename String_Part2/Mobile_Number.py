'''Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.'''

number = input("Enter Contact Number: ")

count = 0

for i in number :
	if i.isdigit() :
		count += 1

print("Total digits:",count)