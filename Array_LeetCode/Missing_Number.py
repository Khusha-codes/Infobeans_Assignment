'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

l = len(lst)

for i in range(l+1):
	if i not in lst:
		print(i)