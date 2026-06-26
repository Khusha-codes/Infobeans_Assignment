'''A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.'''

# using for loop 

n = int(input("Enter a number : "))
count = 0

for i in range(len(str(n))) :
	if (n%10)%2 != 0 :
		count +=1
	n = n//10

print("Number of odd digit :",count)

# using while loop 

n = int(input("Enter a number : "))
count = 0

while n > 0 :
	if (n%10)%2 != 0 :
		count +=1
	n = n//10

print("Number of odd digit :",count)

