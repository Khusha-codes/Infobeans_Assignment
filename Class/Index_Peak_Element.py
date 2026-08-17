arr = []
n = int(input("Enter size: "))

for i in range(n):
	c = int(input("Enter value: "))
	arr.append(c)
print(arr)
peakindex = -1
for i in range(n):
	if i == 0 :
		if n==1 or arr[i] >= arr[i+1]:
			peakindex = i
			break
	elif i == n-1 :
		if arr[i] >= arr[i-1]:
			peakindex = i
			break
	else:
		if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
			peakindex = i
			break
if peakindex != -1 :
	print("Peak index:",peakindex)
	print("Value is",arr[peakindex])
else:
	print("Peak not found")