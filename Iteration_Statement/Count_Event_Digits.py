'''A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.'''

# using for loop 

n = int(input("Enter a number : "))
count = 0

for i in range(len(str(n))) :
	if (n%10)%2 == 0 :
		count +=1
	n = n//10

print("Number of even digit :",count)

# using while loop 

n = int(input("Enter a number : "))
count = 0

while n > 0 :
	if (n%10)%2 == 0 :
		count +=1
	n = n//10

print("Number of even digit :",count)

