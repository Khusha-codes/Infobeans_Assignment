'''A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.'''

# Using for loop

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
count = 1

for i in range(n1,n2+1) :
	if i%10 == 5 :
		count +=1

print("Output: ",count)

# Using for loop

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
count = 1
i = 1

while n1 <= n2:
	if i%10 == 5 :
		count +=1
	n1+=1

print("Output: ",count) 