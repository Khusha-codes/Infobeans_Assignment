n = int(input("Enter Number: "))

for i in range(1,n) :
	for j in range(1,i+1) :
		if j == 1 or j == i :
			print(j,end = " ")
		else :
			print(" ",end = " ")
	print()
for i in range(n) :
	print(i,end = " ")