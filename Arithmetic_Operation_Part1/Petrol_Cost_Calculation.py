'''You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.'''

distance = int(input("Distance ="))
mileage = int(input("Mileage ="))
PPrice = int(input("Petrol price ="))

petrol = distance/mileage
cost = petrol*PPrice

print("Petrol Used =",petrol)
print("Total Cost =",cost)