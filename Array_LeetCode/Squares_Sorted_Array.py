'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

for i in range(n):
	lst[i] = lst[i]**2

while True :
	move = 0
	for i in range(n):
		for j in range(i+1,n):
			if lst[i]>lst[j]:
				move += 1
				temp = lst[j]
				lst[j] = lst[i]
				lst[i] = temp
	if move == 0:
		break

print(lst)