'''A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.'''

import math
n = int(input("Enter number: "))
x = 0
i = 2

if n < 2 :
	print("Not a prime number.")
else:
	while i <= math.sqrt(n) :
		if n%i == 0 :
			print("Not a prime number.")
			x = 1
			break
		i+=1
	else :
		print("Prime number.")
flag = 0
if x == 0 :
	while True :
		i = 2
		n = n+1
		while i <= math.sqrt(n) :
			if n%i == 0 :
				break
			i+=1
		else :
			print("Next Prime number is",n)
			flag = 1
		if flag == 1 :
			break
else :
	while True :
		i = 2
		n = n-1
		while i <= math.sqrt(n) :
			if n%i == 0 :
				break
			i+=1
		else :
			print("previous Prime number is",n)
			flag = 1
		if flag == 1 :
			break
		
