'''A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.'''

import math
n = int(input("Enter number: "))
i = 2

if n < 2 :
	print("Neither prime number nor composite.")
else:
	while i <= math.sqrt(n) :
		if n%i == 0 :
			print("Composite number.")
			break
		i+=1
	else :
		print("Not a composite number.")