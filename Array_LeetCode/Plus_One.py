'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

print(lst)
s = 0

for i in lst:
	s = s*10 + i

s = s + 1

result = []

while s > 0 :
	k = s%10
	result.insert(0,k)
	s = s//10

print(result)
