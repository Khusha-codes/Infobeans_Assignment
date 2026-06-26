'''In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.'''

# using for loop

n = int(input("Enter number : "))
r = n
temp = 0

for i in range(len(str(n+1))) :
	temp = temp + (r%10)**3
	r = r//10

if temp == n :
	print("Armstrong Number")
else :
	print("Not Armstrong Number")

# using while loop

n = int(input("Enter number : "))
i = n
temp = 0

while i > 0:
	temp = temp + (i%10)**3
	i = i//10

if temp == n :
	print("Armstrong Number")
else :
	print("Not Armstrong Number")
