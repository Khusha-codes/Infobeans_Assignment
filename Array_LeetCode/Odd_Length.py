'''Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.'''

n = int(input("Enter number of element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element: ")))

sum = 0
I = 0
while I < len(lst):
	if I %2 == 0:
		for m in range(len(lst)):
			x = I 
			if m + x < len(lst):
				while x >= 0:
					sum += lst[m + x]
					x -= 1
	I +=1

print(sum)