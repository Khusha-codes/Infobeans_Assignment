'''A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.'''

n = int(input("Enter a number :"))
sum = 0
i = 1

while i<=n :
	if n%i == 0 :
		sum += i
	i+=1
print("Factors Sum =",sum)