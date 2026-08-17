n = int(input("Enter number: "))

for i in range(n) :
	j = 0
	while j <= i :
		print(chr(i+65),end ="")
		j+=1
	print()