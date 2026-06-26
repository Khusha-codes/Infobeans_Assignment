'''A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.'''

# using for loop

n = int(input("Enter a Number : "))
d = int(input("Enter a digit : "))
digit = 0

for i in range(len(str(n))) :
	if n%10 == d :
		digit += 1
	n = n//10

print(d,"digit appears",digit,"times")

# using while loop

n = int(input("Enter a Number : "))
d = int(input("Enter a digit : "))
digit = 0

while n > 0 :
	if n%10 == d :
		digit += 1
	n = n//10

print(d,"digit appears",digit,"times")