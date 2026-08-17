'''A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.'''

# Using for loop

n = int(input("Enter Number: "))
square = 0

for i in range(n) :
	square+=n

if n%10 == square%10 :
	print("Automorphic number.")
else :
	print("Not a Automorphic number.")


# Using for loop

n = int(input("Enter Number: "))
temp = n
square = 0

while temp > 0 :
	square+=n
	temp-=1

if n%10 == square%10 :
	print("Automorphic number.")
else :
	print("Not a Automorphic number.") 

