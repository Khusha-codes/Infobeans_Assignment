'''A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible'''

percentage = int(input("Enter attendance percentage "))

if percentage >= 75 :
	print("Status: Eligible")
elif percentage >= 60 :
	print("Status: Eligible with Warning")
else :
	print("Status: Not Eligible")