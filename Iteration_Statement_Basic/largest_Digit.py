'''A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.'''

n = int(input("Enter a number : "))
digit = n%10

while n>0:
	if n%10 > digit :
		digit = n%10
	n = n//10
print("Largest Digit =",digit)