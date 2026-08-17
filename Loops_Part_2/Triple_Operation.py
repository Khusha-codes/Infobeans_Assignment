'''A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime'''

import math
n = int(input("Enter a number: "))
temp = n
sum = 0
rev = 0

while temp > 0:
	sum = sum + temp%10
	rev = rev +temp%10
	rev = rev*10
	temp = temp//10

rev = rev/10
diff = abs(n - rev)
final = sum + diff

print("Sun of Digits =",sum)
print("Reverse =",rev)
print("Difference =",diff)
print("Final Result =",final)

i = 2

while i < math.sqrt(final+1) :
	if final%i == 0 :
		print("Not Prime Number.")
		break
	i+=1
else :
	print("Prime Number.")