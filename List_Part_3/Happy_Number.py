'''Store numbers in a list and identify Happy Numbers.

A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.'''

n = int(input("Enter number: "))
S = 0
happ = n

while S != 1 :
	S = 0
	while happ > 0 :
		S += (happ%10)**2
		happ = happ//10
	if S == n :
		print("Non-Happy Number.")
		break
	happ = S
else :
	print("Happy Number.")
	