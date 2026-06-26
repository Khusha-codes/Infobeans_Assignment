'''The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax'''

income = int(input("Enter annual income: "))

if income<= 250000 :
	print("No tax")
elif income <= 500000 :
	print("tax payable :",income/20)
elif income <= 1000000 :
	print("tax payable :",income/5)
else :
	print("tax payable :",income*(3/10))