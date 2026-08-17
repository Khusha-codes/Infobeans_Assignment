'''Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.'''

import math
n = int(input("Enter Number: "))

while True :
	i = 2
	while i <= math.sqrt(n+1):
		if (n+1)%i == 0 :
			break
		i+=1
	else :
		print("Next Prime Cabin =",n+1)
		break
	n+=1