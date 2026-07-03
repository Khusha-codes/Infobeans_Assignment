'''A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

import math
for k in range(a,b+1) :
	i = 2
	while i <= math.sqrt(k):
		if k%i == 0 :
			break
		i+=1
	else :
		print(k)