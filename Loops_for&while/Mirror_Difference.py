'''Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected'''

# Using for loop

n = int(input("Enter Number: "))
temp = n
rev = 0

for i in range(len(str(n))) :
	rev += temp%10
	if temp > 10 :
		rev = rev*10
	temp = temp//10

print("Reverse =",rev)
print("Difference =",abs(n - rev))
print("Digits =",len(str(abs(n- rev))))
if n == rev :
	print("Perfect Match.")
else :
	print("Verified.")

# Using while loop

n = int(input("Enter Number: "))
rev = 0
temp = n

while temp>0 :
	rev += temp%10
	if temp > 10 :
	 rev = rev*10
	temp = temp//10

print("Reverse =",rev)
print("Difference =",abs(n - rev))
print("Digits =",len(str(abs(n - rev))))
if n == rev :
	print("Verified.")
else :
	print("Verified.")