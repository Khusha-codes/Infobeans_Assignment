''' An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.'''

cvalue = int(input("Card Value : "))
usertype = input("User Type(premium or regular) : ")

if cvalue >= 5000 :
	if usertype.lower() == "premium" :
		print("Final Amount =",(cvalue - cvalue/5))
	else :
		print("Final Amount =",(cvalue - cvalue/10))
else :
	if cvalue >= 2000 :
		print("Final Amount =",(cvalue - cvalue/20))
	else :
		print("No discount is applied.")