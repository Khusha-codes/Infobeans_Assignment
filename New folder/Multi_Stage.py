'''A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not'''

import math
n = int(input("Enter Number: "))
temp = n
sum = 0
product = 1
digit = 0

while temp > 0 :
	sum = sum + temp%10
	product = product*(temp%10)
	temp = temp//10

diff = abs(sum - product)
digit = len(str(diff))
final = diff + digit

print("Sum =",sum)
print("Product =",product)
print("Difference =",diff)
print("Digits =",digit)
print("Final Result =",final)

i = 2

while i > math.sqrt(final) :
	if final%i == 0 :
		print("Not prime")
		break
	i+=1
else :
	print("Prime")
