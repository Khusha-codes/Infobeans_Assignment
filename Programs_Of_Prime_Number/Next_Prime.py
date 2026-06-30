'''A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.'''

import math
x = int(input("Enter a number: "))
flag = 0
n = x+1

if x < 2 :
	print("Next Prime = 2 ")
else :
	while True :
		i = 2
		while i <= math.sqrt(n) :
			if n%i == 0 :
				break
			i = i + 1
		else :
			print("Next Prime number is",n)
			break
		n = n + 1


		 