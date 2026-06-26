'''An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.'''

# using for loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

if start < end :
	for i in range(start,end+1):
		if i == end :
			print(i)
		else :
			print(i,end="->")
elif start > end :
	for i in range(start,end-1,-1):
		if i == end :
			print(i)
		else :
			print(i,end="->")
else :
	print("Already on the same floor.")
print("")

# using while loop

start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

if start < end :
	while start<=end :
		if start == end :
			print(start)
		else :
			print(start,end="->")
		start+=1
elif start > end :
	while start>=end :
		if start == end :
			print(start)
		else :
			print(start,end="->")
		start-=1
else :
	print("Already on the same floor.")

