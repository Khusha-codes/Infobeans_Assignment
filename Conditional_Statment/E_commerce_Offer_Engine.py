''' An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon'''

cart = int(input("Enter Cart Value : "))

if cart >= 500 :
	print("Free delivery applied.")
	if cart >= 1000 :
		print("Discount coupon unlocked.")