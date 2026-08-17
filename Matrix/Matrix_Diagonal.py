'''=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit'''

while true :
	print('Menu')
	print("1. Display Main Diagonal Elements")
	print("2. Display Secondary Diagonal Elements")
	print("3. Compare Main and Secondary Diagonal Sums")
	print("4. Exit\n")
	
	n = int(input("Enter your choice: "))

	match n :
		case 1 :
			row = int(input("Enter number of row: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(row):
					row.append(int(inpunt()))
				A.append(row)

			print("Main Diagonal Elements are")
			for i in range(len(A)):
				print(A[i][i],end = " ")
			print()

		case 2 :
			row = int(input("Enter number of rows: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(row):
					row.append(int(inpunt()))
				A.append(row)

			print("Secondary Diagonal Elements are: ")
			for i in range(len(A)) :
				for j in range(len(i)):
					if i + j = row - 1 :
						print(A[i][j],end = " ")
			print()

		case 3 :
			row = int(input("Enter number of rows: "))
			
			A = []
			print("Enter Matrix A:")
			for i in range(row):
				row = []
				for j in range(row):
					row.append(int(inpunt()))
				A.append(row)

			smd = 0
			for i in range(len(A)):
				smd +=A[i][i]

			ssd = 0
			for i in range(len(A)) :
				for j in range(len(i)):
					if i + j = row - 1 :
						ssd += A[i][j]
						
			print("Main Diagonal Sum",smd)
			print("Secondary Diagonal Sum",ssd)
		
		case 4 :
			print("Thank You for Using Matrix Diagonal Analysis System")
			break 


			


