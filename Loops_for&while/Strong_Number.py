'''A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.'''

# Using for loop

n = int(input("Enter Number: "))
temp = 0
m = 1
fact = 1

for i in range(len(str(n))) :
	m = i%10
	for i in range(1,m+1):
		fact = fact*i
	temp += fact
	fact = 1

if temp == n :
	print("Strong Number.")
else :
	print("Not a Strong Number.")

# Using for loop

n = int(input("Enter Number: "))
i = n
temp = 0
m = 1
fact = 1

while i > 0:
	m = i%10
	while m>0 :
		fact = fact*i
		m//10
	temp += fact
	fact = 1
	i//10

if temp == n :
	print("Strong Number.")
else :
	print("Not a Strong Number.")

