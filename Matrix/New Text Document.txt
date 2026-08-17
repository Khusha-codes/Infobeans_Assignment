'''=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.'''

while true :
	print('Menu')
	print("1. Add Two Matrices")
	print("2. Subtract Two Matrices")
	print("3. Compare Two Matrices")
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

			B = []
			print("Enter Matrix B:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				B.append(row)

			S = []
			for i in range(row):
				row = []
				for j in range(col):
					row.append(A[i][j] + B[i][j])
				B.append(row)

			print("Result Matrix:")
			for row in S:
				print(*row)

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

			B = []
			print("Enter Matrix B:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				B.append(row)

			S = []
			for i in range(row):
				row = []
				for j in range(col):
					row.append(A[i][j] - B[i][j])
				B.append(row)

			print("Result Matrix:")
			for row in S:
				print(*row)

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

			B = []
			print("Enter Matrix B:")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				B.append(row)

			flag = 1
			for row in A :
				fow val in row :
					if A[row][val] != B[row][val] :
						print("Matrices are Not Equal")
						flag = 0
						break 
				if flag = 0 :
					break
			else :
				print("Matrices are Equal")

		case 4 :
			print("Thank You for Using Matrix Operations Management System")
			break
				