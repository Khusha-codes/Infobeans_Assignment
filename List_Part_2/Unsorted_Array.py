'''Given an unsorted array arr[] of size N having both negative and positive integers.
The task is place all negative element at the end of array without changing the order of positive element and negative element.'''

n = int(input("Enter Size of array: "))
l = []
for i in range(n):
	x = int(input("Enter element: "))
	l.append(x)
n = []
for i in l[ : ] :
	if i < 0 :
		n.append(i)
		l.remove(i)
result = l + n
print("Output:")
print(result)		