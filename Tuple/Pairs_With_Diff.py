'''Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.'''

N = int(input("Enter number of element: "))
K = int(input("Age difference: "))
lst = []
for i in range(N):
	lst.append(int(input("Enter element: ")))
A = tuple(lst)

count = 0
for x in A :
	for y in A :
		if x - y == K :
			count += 1 
print(count)