n = int(input("Enter Number: "))

k = 0
for i in range(n) :
	for j in range(i) :
		print(chr(97+k),end = "")
		k+=1
	print()

