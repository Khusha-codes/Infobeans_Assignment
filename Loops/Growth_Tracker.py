n = int(input("Enter a number: "))

n1 = 0
n2 = 1
population = 0
greater = 0
print(n1,end =" ")
for i in range(n-1) :
	population = population + n2
	if n2 > 5 :
		greater +=1
	print(n2,end =" ")
	temp = n2 
	n2 = n2 + n1
	n1 = temp 
print()
print("Total Population =",population)
print("Months with population > 5 =",greater)
