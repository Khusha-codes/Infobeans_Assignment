'''A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.'''

# using for loop

n = int(input("Enter : "))

for i in range(1,11):
	print(n,"x",i,"=",n*i)

# using while loop

n = int(input("Enter : "))
i = 1

while i<=10:
	print(n,"x",i,"=",n*i)
	i+=1
