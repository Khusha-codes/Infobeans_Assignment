'''You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

👉 Important Condition:
If the Basic Salary is not entered, the system should display:
"Please enter basic salary first"
and should not perform any further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction

* Salary > 50000 → 10% tax
* Otherwise → 5% tax
  5 → Display Salary Slip
  6 → Exit'''

salary = None
while True :
	print("1. Basic Salary")
	print("2. HRA and DA")
	print("3. Net Salary")
	print("4. Tax Deduction")
	print("5. Salary Slip")
	print("6. Exit")

	n = int(input("Enter your choice: "))

	match n :
		case 1 :
			salary = int(input("Enter Basic Salary: "))
			print("Basic Salary recorded successfully")	
			HRA = salary/5
			DA =  salary/10
			net_salary = salary + HRA + DA
			if salary > 50000 :
				tax = salary/10
			else :
				tax = salary/20	
			final_salary = net_salary - tax	
			print("")

		case 2 :
			if salary == None :
				print("Please enter basic salary first")
			else :
				print("HRA:",HRA)
				print("DA:",DA)
				if net_salary > 50000 :
					tax = net_salary/10
				else :
					tax = net_salary/20
				final_salary = net_salary - tax
				print("")
		
		case 3 :
			if salary == None :
				print("Please enter basic salary first")
			else :
				print("Net Salary (before tax):",net_salary)
				print("")

		case 4 :
			if salary == None :
				print("Please enter basic salary first")
			else :
				print("Tax:",tax)
				print("")

		case 5 :
			if salary == None :
				print("Please enter basic salary first")
			else :
				print("Basic Salary:",salary)
				print("HRA:",HRA)
				print("DA",DA)
				print("Net Salary:",net_salary)
				print("Tax:",tax)
				print("Final Salary:",final_salary)
				print("")

		case 6 :
			print("Exiting program... Thank you!")
			break

		case __ :
			print("Invalid choice. Please try again.")
			print("")