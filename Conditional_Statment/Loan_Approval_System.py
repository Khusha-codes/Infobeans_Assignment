'''1. A bank wants to automate its loan approval process. The system should take salary,
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000,
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans.
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected.
If the salary is less than 30000, the loan should be rejected. Display the final loan status.'''

salary = int(input("Enter Salary : "))
CS = int(input("Enter Credit Score : "))
loans = int(input("Existing Loans : "))

if salary >= 3000 :
	if CS >= 750 :
		print("Loan Approved")
	else :
		if loans < 2 :
			print("Loan Approved")
		else :
			print("Loan Rejected")
else :
	print("Loan Rejected")