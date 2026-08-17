n = int(input("Enter number: "))

for i in range(n) :
	j = 0
	k = 0
	while j <= i :
		print(chr(k+97),end ="")
		j+=1
		k+=1
	print()
