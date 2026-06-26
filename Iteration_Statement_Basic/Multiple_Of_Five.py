'''A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.'''

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
count = 0

if n1 < n2 :
	while n1<=n2 :
		if n1%5 == 0:
			count+=1
		n1 = n1 + 1
else :
	while n1>=n2 :
		if n1%5 == 0:
			count+=1
		n1 = n1 - 1

print("Number divisible by 5 between ",n1,"and",n2,"are",count)