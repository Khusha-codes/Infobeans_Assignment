'''A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.'''

n = int(input("Enter number : "))
count = 0
i = 1

while i<=n :
	if n%i == 0 :
		count+=1
	i+=1
print("Factors Count =",count)