'''=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit'''

while true :
	print('Menu')
	print("1. Count Armstrong Numbers Row-wise")
	print("2. Count Palindrome Numbers Column-wise")
	print("3. Display Average of Each Row")
	print("4. Exit\n")
	
	n = int(input("Enter your choice: "))

	match n :
		case 1 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for i in range(row):
				rs = 0
				for j in range(col):
					l = str(j)
					S = 0
					temp = j
					while temp > 0:
						S += (temp%10)**l
						temp//10
					if S == j :
						rs+=1
				print("")

		case 2 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for j in range(col):
				cp = 0
				for row in A:
					temp = str(A[row][j])
					pall = temp[::-1]
					if temp == pall :
						cp +=1
				print("")

		case 3 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for row in A:
				rs = 0
				for val in row:
					rs += val
				rs = rs/len(row)
				print(" Average of",row,"Row",rs)

		case 4 :
			print("Thank You for Using Matrix Quality Check System")
			break
				