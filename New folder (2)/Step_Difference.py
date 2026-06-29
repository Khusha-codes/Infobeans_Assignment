'''A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number'''

# Using for loop

n = int(input("Enter Number: "))
temp = n
rev = 0
sum = 0
largest = 0
length = len(str(n))

for i in range(length) :
	rev += temp%10
	if temp > 10 :
		rev = rev*10
	temp = temp//10

print("Step_Differences:",end = " ")
d1 = 0
d2 = 0

for i in range(length - 1 ) :
	d1 = rev%10
	rev = rev//10
	d2 = rev%10
	print(abs(d1 - d2),end=" ")
	sum += abs(d1 - d2)
	if abs(d1 - d2) > largest :
		largest = abs(d1 - d2)


print("\nSum =", sum)
print("Largest =",largest)
if sum//length == 0 :
	print("Balanced Number.")
else :
	print("Unbalanced Number.")

# Using while loop

n = int(input("Enter Number: "))
temp = n
rev = 0
sum = 0
largest = 0
length = len(str(n)) 

while temp > 0:
	rev += temp%10
	if temp > 10 :
		rev = rev*10
	temp = temp//10

print("Step_Differences:",end = " ")
d1 = 0
d2 = 0

while length > 0 :
	d1 = rev%10
	rev = rev//10
	d2 = rev%10
	print(abs(d1 - d2),end=" ")
	sum += abs(d1 - d2)
	if abs(d1 - d2) > largest :
		largest = abs(d1 - d2)
	length-=1

length = len(str(n))
print("\nSum =", sum)
print("Largest =",largest)
if sum//length == 0 :
	print("Balanced Number.")
else :
	print("Unbalanced Number.")

