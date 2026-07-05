n = int(input("Enter Number : "))

k = 1
while k <= n :
	j = 1
	while j <= n-k :
		print(" ",end = " ")
		j+=1

	j = 1
	while j <= k :
		if j%2 == 0 :
			print(0,end = " ")
		else :
			print(1,end = " ")
		j+=1 
	print()
	k+=1