'''The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit'''

unit = int(input("Enter units consumed: "))
bill = 0

for i in range(1,unit+1):
	if i < 101 :
		bill = bill + 5	
	elif i < 201 :
		bill = bill + 7
	else :
		bill = bill + 10

print("Total Electricity Bill: ₹",bill)
