'''An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount'''

amount = int(input("Enter purchase amount : "))

if amount > 5000 :
	print("Final Amount : ₹",(amount - (amount/5)))
elif amount > 2000 :
	print("Final Amount : ₹",(amount - (amount/10)))
else :
	print("Final Amount : ₹",(amount - (amount/20)))