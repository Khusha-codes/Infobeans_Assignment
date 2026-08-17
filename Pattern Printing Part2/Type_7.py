n = int(input("Enter a number: "))

for i in range(n) :
	j = 0
	while j <= i :
		if i%2 == 0 :
			print(1,end = "")
		else :
			print(0,end = "")
		j+=1
	print()