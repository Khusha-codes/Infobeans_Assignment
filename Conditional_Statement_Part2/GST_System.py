'''A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added'''

amount = int(input("Enter bill amount: "))

if amount<=1000:
   print("Final bill Amount:",(amount+amount/20))
elif amount <= 5000:
	if amount >= 3000 :
		print("Final bill Amount:",(amount+amount*(12/100))+200)
	else :
		print("Final bill Amount:",(amount+amount*(12/100)))
else :
	print("Final bill Amount:",(amount+amount*(18/100))+200)