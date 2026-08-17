'''Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.'''

pw = input("Enter password: ")
temp = ""

for ch in pw :
	if ch not in temp :
		temp += ch
print("There are",len(temp),"unique characters in password")