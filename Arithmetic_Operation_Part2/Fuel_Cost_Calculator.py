'''A Python program that:
Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.'''

dis = int(input("Distance = "))
mlg = int(input("Mileage = "))
pp = int(input("Petrol Price = "))

cost = (dis/mlg)*pp

print("Cost",cost)