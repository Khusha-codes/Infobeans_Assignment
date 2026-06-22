'''A Python program that:
Accepts cost price and selling price.
Calculates profit/loss and percentage.'''

cp = int(input("Cost Price = "))
sp = int(input("Selling Price = "))

prf = sp - cp
prfper = (prf*100)/cp

print("Profit = ",prf)
print("Profit % = ",prfper)