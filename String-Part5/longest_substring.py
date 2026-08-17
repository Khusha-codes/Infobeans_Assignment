'''Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.'''

id = input("Enter ID: ")
temp = ""
long = ""
for i in id :
	if i not in temp :
		temp+=i
	else :
		if len(temp) > len(long) :
			long = temp
			temp = ""
		else :
			temp = ""

print("Longest substring containing is",long)