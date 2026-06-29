'''Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.'''

# Using For loop

import math
n = int(input("Enter Number: "))

for i in range(2,int(math.sqrt(n))) :
	if n%i == 0:
		print("Not a Prime Number.")
		break
else:
	print("Prime Number.")

# Using while loop

import math
n = int(input("Enter Number: "))
i = 2

while i <= int(math.sqrt(n)) :
	if n%i == 0:
		print("Not a Prime Number.")
		break
	i+=1
else:
	print("Prime Number.")

