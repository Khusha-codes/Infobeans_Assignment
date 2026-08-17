'''Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length'''

N = int(input("Enter number of element: "))
lst = []
for n in range(N) :
	x = int(input("Enter value: "))
	lst.append(x)
lst = sorted(lst)
max = 0
temp = 1
for i in range(N-1):
	if lst[i] + 1 == lst[i+1] :
		temp += 1
	else :
		if temp > max :
			max = temp
		temp = 1
if max != 1 :
	print("Longest Consecutive Length =",max)
else :
	print("No Consecutive Sequence")
	