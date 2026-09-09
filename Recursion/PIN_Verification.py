'''A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.'''

def pal(n,m=0):
	m = m*10+n%10
	if len(str(m)) >= len(str(n)):
		if len(str(m)) > len(str(n)):
			m = m//10
		if m == n:
			return "Palindrome Number"
		else:
			return "Not a Palindrome Number" 
	return pal(n//10,m)

n = int(input("Enter a number: "))
print(pal(n))