'''Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

result = []

first = 0
for i in range(n-1):
	if lst[i] >lst[i+1]:
		first = i
		break

last = 0
for i in range(n-1,0,-1):
	if lst[i] < lst[i-1]:
		last = i+1
		break


count = 0
for i in range(first,last):
	count += 1
		
print(count)