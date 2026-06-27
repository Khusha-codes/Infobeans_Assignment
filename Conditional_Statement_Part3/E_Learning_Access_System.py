'''An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.'''

subscription = input("Subscription = ")
progress = int(input("Progress = "))
score = int(input("Test Score = "))

if subscription.lower() == "premium" :
	if progress >= 80 :
		if score >= 70 :
			print("Certificate unlock.")
		else :
			print("Retry.")
	else :
		print("Do complete course.")
elif subscription.lower() == "basic" :
	if progress >= 50 :
		print("Limited access.")
	else :
		print("Lock contect.")
else :
	print("Deny access.")
