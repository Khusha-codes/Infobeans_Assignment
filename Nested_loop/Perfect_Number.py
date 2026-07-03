'''A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

for k in range(a,b+1):
	i = 1
	sum = 0
	while i < k :
		if k%i == 0 :
			sum += i
		i+=1
	if k == sum :
		print(k)
