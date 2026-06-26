''' A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program'''

age = int(input("Enter Age : "))
bmi = int(input("Enter BMI : "))

if age >= 18 :
	print("Gym access granted.")

if bmi > 25 :
	print("Enroll in weight loss program.")