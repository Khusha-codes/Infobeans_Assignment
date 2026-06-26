'''A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*'''

# using for loop 

n = int(input("Enter a number : "))
count = 0

for i in range(len(str(n))) :
	if (n%10)%2 != 0 :
		count = 1
	n = n//10

if count == 0 :
	print("All Even")
else :
	print("Not All Even")

# using while loop 

n = int(input("Enter a number : "))
count = 0

while n > 0 :
	if (n%10)%2 != 0 :
		count = 1
	n = n//10

if count == 0 :
	print("All Even")
else :
	print("Not All Even")

