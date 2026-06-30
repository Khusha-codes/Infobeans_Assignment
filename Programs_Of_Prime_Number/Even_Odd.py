'''A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not'''

import math
n = int(input("Enter Number: "))
even = 0
odd = 0

while n > 0 :
	if (n%10)%2 == 0 :
		even+=1
	else :
		odd+=1
	n = n//10

diff = abs(even - odd)
print("Even Count =",even)
print("Odd count =",odd)
print("Difference =",diff)

i = 2
if diff < 2:
	print("Not Prime Number")
else :
	while i < math.sqrt(diff) :
		if diff%i == 0 :
			print("Not Prime Number")
			break
		i+=1
	else :
		print("Prime Number")