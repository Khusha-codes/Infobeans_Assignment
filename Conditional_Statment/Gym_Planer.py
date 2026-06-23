'''A gym provides personalized plans based on age, weight, and fitness goal.
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or
 equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.'''

age = int(input("Age : "))
weight = int(input("Weight : "))
goal = input("Goal(weight loss or muscle gain) : ")

if age >= 18 :
	if weight >= 80 :
		if goal.lower() == "weight loss" :
			print("Plane = Cardio Plan.")
		else :
			print("Plane = Strength Plan.")
	else :
		print("Plane = General Fitness Plan.")
else :
	print("Not Allowed.")