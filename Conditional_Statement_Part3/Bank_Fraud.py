'''A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.'''

TA = int(input("Enter Transaction Amount : "))
loc = input("Location : ")
age = int(input("Account Age : "))

if TA >= 10000 :
	if loc.lower() == "international" :





	else :
		if TA >50000 :
			if age > 2 :
				print("Allow.")
			else :
				print("Flagged.")
		else:
			print("Allow.")
