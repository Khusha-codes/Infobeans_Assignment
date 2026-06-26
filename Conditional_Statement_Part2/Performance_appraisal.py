'''A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.'''

salary = int(input("Enter salary: "))
rating = int(input("Enter rating: "))

if rating == 5 :
	if salary <= 20000 :
		print("Revised Salary: ₹",(salary + (salary/4) + 2000))
	else :
		print("Revised Salary: ₹",(salary + salary/4))
elif rating == 4 :
	if salary <= 20000 :
		print("Revised Salary: ₹",(salary + (salary/5) + 2000))
	else :
		print("Revised Salary: ₹",(salary + salary/5))
elif rating == 3 :
	print("Revised Salary: ₹",(salary + salary/10))
elif rating == 2 :
	print("Revised Salary: ₹",(salary + salary/20))
else :
	print("Revised Salary: ₹",(salary))