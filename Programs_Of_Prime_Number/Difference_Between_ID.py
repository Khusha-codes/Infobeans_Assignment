'''A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.'''

import math
n = int(input("Enter Number: "))
temp = n
flag = 0

while True :
	i = 2
	n = n+1
	while i <= math.sqrt(n) :
		if n%i == 0 :
			break
		i+=1
	else :
		print("Next Prime number is",n)
		print("Gap =", n - temp)
		flag = 1
	
	if flag == 1 :
		break
