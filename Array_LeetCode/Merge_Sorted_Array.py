'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''

n1 = int(input("Enter number of element of list 1: "))
lst1 = []

for i in range(n1):
	lst1.append(int(input("Enter element of list 1: ")))

n2 = int(input("Enter number of element of list 2: "))
lst2 = []

for i in range(n2):
	lst2.append(int(input("Enter element of list 2: ")))

for x in lst2:
	lst1.append(x)

while True :
	count = 0
	for i in range(len(lst2)-1) :
		if lst1[i] > lst1[i+1] :
			count += 1
			temp = lst1[i]
			lst1[i] = lst1[i+1]
			lst1[i+1] = temp
	if count == 0 :
		break

print(lst1)