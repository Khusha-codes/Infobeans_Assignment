'''A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.'''

a = int(input("Enter Starting Number: "))
b = int(input("Enter Ending Number: "))

for k in range(a,b+1) :
	rev = 0
	temp = k
	while temp > 0 :
		rev = rev*10 + temp%10
		temp = temp//10
	if rev == k :
		print(k)