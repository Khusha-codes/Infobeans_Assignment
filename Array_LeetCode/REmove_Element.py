'''Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

n = int(input("Enter number of element: "))
nums = []

for i in range(n):
	nums.append(int(input("Enter element: ")))

print(nums)

val = int(input("Enter value: "))

for i in nums[:]:
	if i == val:
		nums.remove(i)
k = len(nums)

print(k,", num =",nums)