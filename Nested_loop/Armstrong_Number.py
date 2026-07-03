'''A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

for k in range(a,b+1) :
	l = len(str(k))
	temp = k
	sum = 0
	while temp > 0 :
		sum = sum + (temp%10)**l
		temp = temp//10
	if k == sum :
		print(k)