'''A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.'''

salary = int(input("Salary = "))
score = int(input("Credit Score = "))
loans = int(input("Existing Loans = "))

if salary >= 30000 :
	if score >= 750 :
		if loans == 0 :
			print("Low risk.")
		elif loans <= 2 :
			print("Medium risk.")
		else :
			print("High risk.")
	else :
		if salary >= 50000 :
			if score >= 650 :
				print("Medium risk")
			else :
				print("High risk")
else :
	print("Not eligible")
		