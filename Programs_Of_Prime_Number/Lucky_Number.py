'''A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number'''

import math 
n = int(input("Enter number: "))
sum = 0
temp = n 

while temp > 0:
	sum = sum + temp%10
	temp = temp//10

print("Sum =",sum)

i = 2
while i <= math.sqrt(sum) :
	if sum%i == 0 :
		print("Not Lucky Number")
		break
	i+=1
else :
	print("Lucky Number")