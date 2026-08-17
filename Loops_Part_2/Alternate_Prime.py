'''Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not'''

import math
n = int(input("Enter a number:"))
sum = 0

while n > 0:
	sum = sum + n%10
	n = n//100

print("Alternate Sum =",sum)

i = 2

while i <= math.sqrt(sum):
	if sum%i == 0 :
		print("Not Prime")
		break
	i+=1
else :
	print("prime")