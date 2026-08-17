n = int(input("Enter a number: "))

for p in range(1, n+1) :
	for q in range(1,n+1) :
		if (p+q)%2 == 0 :
			print(1,end = "")
		else :
			print(0,end = "")
