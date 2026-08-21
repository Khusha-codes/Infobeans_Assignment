n1 = int(input("Enter number of element in first list: "))
nums1 = []

for I in range(n1):
	nums1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of element in second list: "))
nums2 = []

for I in range(n2):
	nums2.append(int(input("Enter element: ")))

result = []

for i in nums1[:] :
	for j in nums2[:] :
		if i == j :
			result.append(i)
			nums1.remove(i)
			nums2.remove(j)
			break
print(result)