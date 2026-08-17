'''MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit'''

n = int(input("Enter side: "))
matrix = []

for I in range(n):
	lst = []
	for j in range(n):
		lst.append(int(input("Enter element: ")))
	matrix.append(lst)

count_eve = 0
for r in range(n):
	for i in range(r+1,n) :
		if matrix[r][i]%2 == 0 :
			count_eve += 1

print("Even Numbers Above Main Diagonal =",count_eve)
print()

count_odd = 0
for r in range(n):
	for i in range(r):
		if matrix[r][i]%2 != 0:
			count_odd +=1

print("Odd Numbers Below Main Diagonal =",count_odd)
print()

print("Boundary Elements:")
for r in range(n):
	for p in range(n):
		if r == 0 or p == 0 or r == n-1 or p == n-1:
			print(matrix[r][p],end = " ")