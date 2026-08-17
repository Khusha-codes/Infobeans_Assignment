n = int(input("Enter number: "))

for i in range(1,n+1) :
	j = 1
	while j <= i :
		print(chr(j+65))
		j+=1