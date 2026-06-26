'''A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.'''

n = int(input("Enter a number :"))
p = int(input("Enter power of the number :"))
result = n
i = 1

while i<p :
	result = result*n
	i+=1
print("Output = ",result)