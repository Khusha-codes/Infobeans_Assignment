n = int(input("Enter size: "))
if n == 0 :
	print(-1)
else :
	arr = []
	for i in range(n):
		x = int(input("Enter element: "))
		arr.append(x)
	leadersum = 0
	for i in range(n):
		isleader = True
		for j in range(i+1,n):
			if arr[i]<=arr[j]:
				isleader = False
				break
		if isleader :
			leadersum += arr[i]
	print("Sum is",leadersum)