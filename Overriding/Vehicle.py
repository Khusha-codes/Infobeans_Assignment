'''Create a parent class Vehicle with:

vehicle_no
brand
rent_per_day

Create two child classes:

Car
Bike


Requirements
Take vehicle details and number of rental days from the user.
Use super() to initialize common attributes.
Create a method calculate_rent(days) in the parent class.
Override the method in both child classes.
For a Car, add ₹500 service charge to the rental amount.
For a Bike, add ₹200 service charge.
Display the final rental amount.'''

class Vehical:
    def __init__(self,no,brand,rent):
        self.no = no
        self.brand = brand
        self.rent = rent

    def calculate_rent(self,day):
        self.rpd = self.rent*day

class Car(Vehical):
    def __init__(self, no, brand, rent):
        super().__init__(no, brand, rent)

    def calculate_rent(self,day):
            self.rpd = self.rent*day+500

class Bike(Vehical):
    def __init__(self, no, brand, rent):
        super().__init__(no, brand, rent)

    def calculate_rent(self,day):
            self.rpd = self.rent*day+200

no = input("Enter Vehicle Number: ")
brand = input("Enter Brand: ")
rent = int(input("Enter Rent Per Day: "))
day = int(input("Enter Number of Days: "))
type = input("Enter Vehicle Type: ").lower()

if type == "car":
     obj = Car(no,brand,rent)
else:
     obj = Bike(no,brand,rent)
obj.calculate_rent(day)
print("----- Rental Details -----")
print("Vehicle Number : ",obj.no)
print("Brand          : ",obj.brand)
print("Rent Per Day   : ",obj.rent)
print("Number of Days : ",day)
print("Vehicle Type   : ",type)
print("Final Amount   : ",obj.rpd)
