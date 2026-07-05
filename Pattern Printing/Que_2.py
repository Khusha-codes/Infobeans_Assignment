import math
n = int(input("Enter Number: "))

i = 1
while i <= n :
	print("For",i)
	print("Square =",i**2,end = ",")
	print("Cube =",i**3,end = " & ")
	print("Square =",math.sqrt(i))
	i+=1