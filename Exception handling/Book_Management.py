'''
Mohan is a librarian and wants to develop a small Python application to manage
book purchases. The system should ensure that a customer cannot purchase more
books than the quantity currently available.

Create a class named Book with the following attributes:

1. book_id       - String
2. book_title   - String
3. author_name  - String
4. price        - float
5. quantity     - int

Create a custom exception class named:

InvalidQuantityException

Requirements:

1. Create the Book class with the above attributes.

2. Create a custom exception InvalidQuantityException by inheriting from
   the built-in Exception class.

3. Create a method purchase(quantity).

4. If the requested purchase quantity is greater than the available quantity,
   raise InvalidQuantityException with the message:

   Quantity not available

5. If the purchase is successful, reduce the available quantity.

6. Display the remaining quantity.

7. Use try-except to handle the custom exception.

8. Quantity purchased must be a positive integer.
'''


class InvalidQuantityException(Exception):
    pass

class Book:

    def __init__(self,id,title,name,price,quantity):
        self.book_id = id
        self.book_title = title
        self.author_name = name
        self.price = price
        self.quantity = quantity

    def purchase(self,qua):
        if qua > self.quantity:
            raise InvalidQuantityException("Quantity not available")
        elif qua < 1 or type(qua) != int:
            raise InvalidQuantityException("Please Enter Valid Quantity")
        else :
            print("Purchase successful")
            self.quantity -= qua
            print("Remaning Quantity",self.quantity)

id = input("Enter Book ID: ")
title = input("Enter Book Title: ")
name = input("Enter Author Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))
obj = Book(id,title,name,price,quantity)
qua = int(input("Enter Quantity to Purchase: "))

try:
    obj.purchase(qua)
except InvalidQuantityException as e:
    print(e)

