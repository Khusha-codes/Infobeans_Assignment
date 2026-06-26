'''A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.'''

n = int(input("Enter a number : "))
digit = n%10

while n>0:
	if n%10 < digit :
		digit = n%10
	n = n//10
print("Smallest Digit =",digit)