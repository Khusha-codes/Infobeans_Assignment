'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''

n = int(input("Enter number of element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element: ")))

j = 0
while j < len(lst):
	k = j + 1
	while k < len(lst) and j < k:
		if lst[j] == lst[k] :
			lst.remove(lst[k])
		k += 1
	j += 1

sum = 0
for i in lst:
	sum += i

print(sum)
