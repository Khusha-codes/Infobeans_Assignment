'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

n = len(lst) + 1
result = []

for i in range(1,n):
	if i not in lst :
		result.append(i)

print(result)