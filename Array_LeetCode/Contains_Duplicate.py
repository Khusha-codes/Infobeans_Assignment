'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

n = int(input("Enter number element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element: ")))

found = False
for I in lst:
	if lst.count(I) > 1:
		found = True
		break
print(found)
