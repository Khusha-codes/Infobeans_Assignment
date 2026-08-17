'''Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.'''

id = input("Enter Ticket ID: ")

for ch in id :
	if id.count(ch) == 1 :
		print("First Non-Repeated Character is",ch)
else :
	print("There is no non-repeating character.")