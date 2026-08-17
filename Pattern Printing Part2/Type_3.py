n = int(input("Enter a number: "))

for i in range(n) :
	j = 0
	while j <= i :
		if j == i :
			print("*")
		else :
			print(" ", end = "")
		j+=1