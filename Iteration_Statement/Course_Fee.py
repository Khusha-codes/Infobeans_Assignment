'''An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount'''

course = input("Enter course category: ")
user = input("Enter user type: ")
fee = None

if course.lower() == "programming" :
	fee = 5000
	if user.lower() == "student" :
		print("Final Corse Fee: ₹",(fee - (fee/5)))
	elif user.lower() == "working professional" :
		print("Final Corse Fee: ₹",(fee - (fee/10)))
	else :
		print("Final Corse Fee: ₹",(fee))
elif course.lower() == "design" :
	fee = 4000
	if user.lower() == "student" :
		print("Final Corse Fee: ₹",(fee - (fee/5)))
	elif user.lower == "working professional" :
		print("Final Corse Fee: ₹",(fee - (fee/10)))
	else :
		print("Final Corse Fee: ₹",(fee))
elif course.lower() == "marketing" :
	fee = 3000
	if user.lower() == "student" :
		print("Final Corse Fee: ₹",(fee - (fee/5)))
	elif user.lower == "working professional" :
		print("Final Corse Fee: ₹",(fee - (fee/10)))
	else :
		print("Final Corse Fee: ₹",(fee))
else : 
	print("No such course found.")