'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

n = int(input("Enter number of element in list: "))
lst = []

for x in range(n):
	lst.append(int(input("Enter element: ")))

for i in range(n) :
	if lst[i] == 0:
		lst.pop(i)
		lst.append(0)

print(lst)