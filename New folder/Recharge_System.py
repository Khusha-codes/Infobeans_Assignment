'''A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.'''

def prime(n,m=2):
	if n/2 < m:
		return "Prime Number"
	if n%m == 0:
		return "Not Prime Number"
	return prime(n,m+1)

n = int(input("Enter Coupon Number: "))
print(prime(n))