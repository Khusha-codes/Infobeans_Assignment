'''A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.'''

marks = int(input("Marks = "))
income = int(input("Income = "))
category = input("Category = ")

if marks >= 85 :
	if income <= 300000 :
		if category.lower != "general":
			print("Full Scholarship.")
		else :
			print("75% Scholarship.")
	else :
		print("50% Scholarship.")
elif marks >= 70 :
	if income <= 200000 :
		print("50% Scholarship.")
else :
	print("25% Scholarship.")