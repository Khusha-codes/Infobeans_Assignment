'''A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction'''

marks = int(input("Enter Marks : "))

if marks>=40 :
	print("Pass")
	if marks>=75 :
		print("Distinction")
else :
	print("Fail")