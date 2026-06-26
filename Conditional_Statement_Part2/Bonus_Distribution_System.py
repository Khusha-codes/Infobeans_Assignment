'''A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus'''

salary = int(input("Enter Salary: "))
experience = int(input("Enter years of experience: "))

if experience > 10 :
	print("Bonus Amount: ₹",salary/5)
elif experience > 5 :
	print("Bonus Amount: ₹",salary/10)
elif experience > 2 :
	print("Bonus Amount: ₹",salary/20)
else :
	print("No Bonus")