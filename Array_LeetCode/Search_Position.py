'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''

n = int(input("Enter number of element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element:")))

print(lst)
t = int(input("Enter target: "))

for I in lst:
	if I == t or I > t:
		print(lst.index(I))
		break
else :
	print(n)
