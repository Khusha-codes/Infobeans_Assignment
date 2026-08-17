'''MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit'''

S = int(input("Enter side of matrix: "))

M = []
for i in range(S):
	lst = []
	for j in range(S):
		lst.append(int(input("Enter element: ")))
	M.append(lst)
print(M)

while True :
	print()
	print("Menu")
	print("1. Find Employee with Highest Total Score")
	print("2. Find Month with Lowest Average Score")
	print("3. Display Employee-wise Maximum Score")
	print("4. Exit")
	print("")
	
	n = int(input("Enter your choice: "))

	match n:
		case 1:
			rsum = []
			for row in M:
				sum = 0
				for i in row :
					sum += i
				rsum.append(sum)
			p = sorted(rsum)[-1]
			print("Employee number having the highest total score is",p)
		case 2:
			lst = []
			for i in range(S) :
				avg = 0
				for row in M :
					avg += row[i]
				lst.append(avg/S)
			print(sorted(lst)[0])
		case 3:
			lst = []
			for row in M :
				max = row[0]
				for i in row :
					if max < i :
						max = i
				lst.append(max)
			print("maximum value present in each row: ",lst)
		case 4:
			print("Thanks for using Matrix Performance Evaluation System.")
			break
