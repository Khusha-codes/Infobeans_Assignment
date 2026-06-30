'''A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1'''

import math
n = int(input("Enter number: "))
count = 0
lower = 9
i = 0

while i <= math.sqrt(n) :
	if n%i == 0 :
		if i == math.sqrt(n) :
			count+=1
		else :
			count+=2
		if i < lower :
			lower = i
print("Factors Count =",count)
print("Smallest Factor =",lower)	