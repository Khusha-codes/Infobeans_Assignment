'''A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.'''

# Using for loop

n = int(input("Enter Number: "))
product = 1

for i in range(1,n+1) :
	if i%2 == 0 :
		product = product*i

print("Output: ",product)

# Using for loop

n = int(input("Enter Number: "))
product = 1
i = 1

while i <= n:
	if i%2 == 0 :
		product = product*i
	i+=1

print("Output: ",product) 