'''A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not'''

import math
n = int(input("Enter number: "))
zero = 0
sum = 0
smallest = 9

while n > 0 :
	sum = sum + n%10
	if n%10 == 0 :
		zero += 1
	if n%10 < smallest :
		smallest = n%10
	n = n//10
final = (sum + zero)*smallest
print("Zero Count =",zero)
print("Sum =",sum)
print("Smallest Digit =",smallest)
print("Final Result =",final)

i = 2
if final < 2:
	print("Not Prime Number")
else :
	while i < math.sqrt(final) :
		if final%i == 0 :
			print("Not Prime Number")
			break
		i+=1
	else :
		print("Prime Number")
