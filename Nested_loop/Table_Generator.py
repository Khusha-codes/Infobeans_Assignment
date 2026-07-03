'''Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.'''

n = int(input("Enter limit: "))
x = 1 

while x <= n :
	y = 1
	while y <= n :
		print(x,"x",y,"=",x*y)
		y += 1
	print("")
	x+=1