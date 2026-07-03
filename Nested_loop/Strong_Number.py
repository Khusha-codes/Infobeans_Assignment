'''A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

for k in range(a,b+1) :
	sum = 0
	while k > 0 :
		i = k%10
		j = 1
		fac = 1
		while j >= i :
			fac = fac*j
			j = j + 1
		sum += fac
		k = k//10
	if sum == k :
		print(k)
