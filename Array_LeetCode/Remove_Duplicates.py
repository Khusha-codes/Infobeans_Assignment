'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.'''

n = int(input("Enter number of element in array: "))
nums = []

for i in range(n):
	nums.append(int(input("Enter element: ")))

expectedNums = []

for i in nums:
	if i not in expectedNums:
		expectedNums.append(i)

k = len(expectedNums)

print(k, end =", num = ")

print(expectedNums)