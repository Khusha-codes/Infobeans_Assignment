'''=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit'''

while true :
	print('Menu')
	print("1. Count Prime Numbers Row-wise")
	print("2. Count Perfect Numbers Column-wise")
	print("3. Display Row-wise Sum")
	print("4. Exit\n")
	
	n = int(input("Enter your choice: "))

	match n :
		case 1 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix :")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for row in A:
				pc = 0
				for j in row :
					x = 2
					while x < j//2 :
						if j%x == 0
							break
						x+=1
					else :
						pc += 1
				print("Row",row,"Prime Count = ",pc)
		case 2 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix :")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for i in range(col) :
				pn = 0
				for row in A :
					for A[row][i] in row :
						

				print("Column",i,"Perfect Number Count = ",pn)
		case 3 :
			row = int(input("Enter number of rows: "))
			col = int(input("Enter number of columns: "))
			
			A = []
			print("Enter Matrix :")
			for i in range(row):
				row = []
				for j in range(col):
					row.append(int(inpunt()))
				A.append(row)

			for row in A:
				S = 0
				for j in row :
					pc += j
				print("Row",row,"Sum = ",S)

		case 4 :
			print("Thank You for Using Matrix Analysis System")
			break


