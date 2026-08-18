'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''

n = int(input("Enter number of element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element: ")))

for I in lst:
	if lst.count(I) == 1:
		print(I)