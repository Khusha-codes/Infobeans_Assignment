'''A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.'''

n = int(input("Enter a number = "))

while n > 0:
	if n < 10 :
		f_digit = n
	n = n//10
print("First Digit =",f_digit)