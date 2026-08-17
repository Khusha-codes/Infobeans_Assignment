'''A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number'''

n = int(input("Enter Number: "))

for i in range(len(str(n))):
	p = n%10
	n = n//10
	q = n%10
	if p < q :
		print("Unstable Number")
		break
else :
	print("Stable Number")