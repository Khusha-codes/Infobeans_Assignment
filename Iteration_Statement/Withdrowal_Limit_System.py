'''A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000'''

balance = int(input("Enter account balance: "))

if balance < 1000 :
	print("Not allowed")
elif balance < 5000 :
	print("Maximum withdrawal Limit: ₹1000")
else :
	print("Maximum withdrawal Limit: ₹5000")