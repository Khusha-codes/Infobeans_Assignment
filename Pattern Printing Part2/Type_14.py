n = int(input("Enter a number: "))

k = 1
for i in range(1,n) :
	j = 0
	while j<i :
		print(k, end = "")
		j+=1
		k+=1
	print()