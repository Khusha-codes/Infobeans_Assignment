'''A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.'''

# With for loop

n = int(input("Enter number of days : "))
points = 0

for i in range(1,n+1):
	points += i

print("Total Points =",points)

# With While loop

n = int(input("Enter number of days : "))
points = 0
i = 1

while i <= n:
	points += i
	i += 1

print("Total Points =",points)
