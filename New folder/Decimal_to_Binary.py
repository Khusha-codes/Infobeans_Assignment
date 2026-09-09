'''An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.
'''

def binary(n):
	if n == 0: 
		return 0
	if n == 1:
		return 1
	return (binary(n//2))*10 + n%2

n = int(input("Enter number: "))
print(binary(n))