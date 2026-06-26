'''System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate'''

marks = int(input("Enter Marks : "))
attendance = int(input("Enter Attendance : "))

if marks >= 40 :
	print("Pass")

if attendance >= 75 :
	print("Eligible for certificate")