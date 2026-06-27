'''A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.'''


amount = float(input("Enter Transaction Amount: "))
location = input("Enter Location (international/domestic): ").lower()
device = input("Device: ")
trans = int(input("Transaction: "))

if amount >= 5000:
	if location == "international":
		if device.lower() == "new" :
			if trans > 3 :
				print("Hight Risk(Block)")
			else :
				print("Medium Risk")
		else :
			print("Medium Risk")
	elif location.lower() == "domestic" :
		if trans > 5 :
			print("Medium Risk")
		else :
			print("Low Risk")
else :
	if device.lower() == "new" :
		print("Medium Risk")
	else :
		print("Low Risk")