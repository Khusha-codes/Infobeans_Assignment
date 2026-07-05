n = int(input("Enter Number: "))

i = n
while i > 0 :
	print(" "*(n-i),end = "")
	j = n
	while j > 0:
		if j > n-i :
			print(j,end = "")
		j-=1
	print()
	i-=1