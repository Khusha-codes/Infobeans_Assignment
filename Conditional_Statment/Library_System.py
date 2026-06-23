'''A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books'''

membership = input("Membership active (yes/no): ")
book = int(input("Books issued: "))

if membership.lower() == "yes" :
	print("Entry allowed.")
	if book < 3:
		print("Can issue more books.")