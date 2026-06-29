'''A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.'''

# Using for loop

n = int(input("Enter Number: "))
found = 0

for i in range(len(str(n))) :
	if n%10 == 0:
		found+=1
	n = n//10

if found == 0 :
	print("Not a Duck Number.")
else :
	print("Duck Number.")


# Using for loop

n = int(input("Enter Number: "))
found = 0

while n > 0 :
	if n%10 == 0:
		found+=1
	n = n//10

if found == 0 :
	print("Not a Duck Number.")
else :
	print("Duck Number.") 
