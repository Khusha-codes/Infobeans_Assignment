'''An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount'''

class product:
    def __init__(self,id,name,quatity,price):
        self.id = id
        self.name = name
        self.quatity = quatity
        self.price = price

    def calculation(self):
        self.total = self.quatity*self.price
        if self.total > 5000:
            self.discount = self.total/10
        else:
            self.discount = self.total/20
        self.amount = self.total - self.discount

    def display(self):
        print("------ Shopping Bill ------")
        print("Product ID        : ",self.id)
        print("Product Name      : ",self.name)
        print("Quantity          : ",self.quatity)
        print("Price Per Item    : ",self.price)
        print("Total Amount      : ",self.total)
        print("Discount          : ",self.discount)
        print("Final Amount      : ",self.amount)

id = input("Enter Product ID : ")
name = input("Enter Product Name : ")
quantity = int(input("Enter Quantity : "))
price = int(input("Enter Price Per Item : "))

cust = product(id,name,quantity,price)
cust.calculation()
cust.display()