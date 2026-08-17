n = int(input("Enter a number: "))

for i in range(n) :
	j = 0 
	while j <= i :
		print(chr(75+i,end = ""))
		j+=1
	print()
