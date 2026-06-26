'''Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth'''

Age = int(input("Enter age: "))

if Age>=18:
	ID = input("Do you have ID (yes/no): ")
	if ID.lower() == "yes" :
		print("Eligible to vote.")
	else :
		print("ID prooof is needed.")
else :
	print("Under Age.")