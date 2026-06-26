'''A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to *find the product of all digits of a number using loops and then check whether the result is even or odd*.'''

# using for loop

n = int(input("Enter a number : "))
product = 1

for i in range(len(str(n))+1) :
	if i != 0 :
		product = product*i

print("Output :",product)
if product%2 == 0 :
	print("Even")
else :
	print("Odd")

# using while loop 

n = int(input("Enter a number : "))
product = 1

while n > 0 :
	if n != 0 :
		product = product*n%10
	n = n//10

print("Output :",product)
if product%2 == 0 :
	print("Even")
else :
	print("Odd")
