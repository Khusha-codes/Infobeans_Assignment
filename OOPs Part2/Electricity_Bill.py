'''An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150'''

class Customer:
    def __init__(self,id,name,unit):
        self.id = id
        self.name = name
        self.unit = unit

    def Calculations(self):
        self.bill = (self.unit*8) + 150

    def display(self):
        print("Customer ID       :",self,id)
        print("Customer Name     :",self.name)
        print("Units Consumed    :".self.unit)
        print("Total Bill Amount :",self.bill)

id = int(input("Enter Customer ID :"))
name = input("Enter Customer name:")
unite = int(input("Enter Unite Consumed:"))

cust = Customer(id.name.unit)
cust.Calculations
cust.display

