n = int(input("Enter a number: "))

n1 = 0
n2 = 1
print(n1,end =" ")
for i in range(n-1) :
	print(n2,end =" ")
	temp = n2 
	n2 = n2 + n1
	n1 = temp 
	
