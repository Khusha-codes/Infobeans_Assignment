'''Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

for k in range(a,b+1) :
	sum = 0
	temp = k**2
	while temp > 0 :
		sum = sum + temp%10
		temp = temp//10
	if k == sum :
		print(k)