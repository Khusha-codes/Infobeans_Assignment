'''A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.'''

vehicle = input("Enter vehicle typey: ")
time = int(input("Enter hours parked: "))
fee = None

if vehicle.lower() == "bus" :
	fee = 50
	if time >= 5 :
		print("Total Parking Fee: ₹",(time*fee) + 100)
	else :
		print("Total Parking Fee: ₹",time*fee)
elif vehicle.lower() == "car" :
	fee = 20
	if time >= 5 :
		print("Total Parking Fee: ₹",(time*fee) + 100)
	else :
		print("Total Parking Fee: ₹",time*fee)
else :
	fee = 10
	if time >= 5 :
		print("Total Parking Fee: ₹",(time*fee) + 100)
	else :
		print("Total Parking Fee: ₹",time*fee)
