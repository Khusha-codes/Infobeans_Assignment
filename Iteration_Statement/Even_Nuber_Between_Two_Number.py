'''A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.'''

# using for loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

for i in range(start,end+1):
	if i%2 == 0 :
		print(i, end = " ")
print("")

# using While loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

while start <= end :
	if start%2 == 0 :
		print(start, end = " ")
	start += 1
