'''A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.'''

# using for loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

if start < end :
	for i in range(start,end+1):
		print(i,end=" ")
else :
	for i in range(start,end-1,-1):
		print(i,end=" ")
print("")

# using while loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

if start < end :
	while start<=end :
		print(start,end=" ")
		start+=1
else :
	while start>=end :
		print(start,end=" ")
		start-=1
