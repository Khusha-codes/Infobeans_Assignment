'''A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.'''

import math
n = int(input("Enter number: "))
i = 2

if n < 2 :
	print("Not a prime number.")
else:
	while i <= math.sqrt(n) :
		if n%i == 0 :
			print("Not a prime number.")
			break
		i+=1
	else :
		print("Prime number.")