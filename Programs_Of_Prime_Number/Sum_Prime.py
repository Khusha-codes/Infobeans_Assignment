'''A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not'''

import math
n = int(input("Enter number: "))
smallest = 9
largest = 0

while n > 0 :
	if n%10 < smallest :
		smallest = n%10
	if n%10 > largest :
		largest = n%10
	n = n//10

sum = largest + smallest
print("Largest =",largest)
print("Smallest =",smallest)
print("Sum =",sum)
i = 2

while i < math.sqrt(sum) :
	if sum%i == 0 :
		print("Not a Prime Number")
		break
	i+=1
else :
	print("Prime Number")