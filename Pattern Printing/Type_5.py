n = int(input("Enter Number: "))

j = 1
while j <= n :
	k = 1
	while k <= j :
		print(chr(64+k),end = " ")
		k+=1
	print()
	j+=1