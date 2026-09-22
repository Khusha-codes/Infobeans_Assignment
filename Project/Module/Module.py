'''Create a Student class inside:

models/student.py

ATTRIBUTES:

* roll_no
* name
* marks

TASKS:

1. Take details of 5 students from the user.
2. Create a Student object for each student.
3. Store all Student objects inside a list.
4. Display all students.
5. Display students whose marks are greater than 60.
6. Find the student having the highest marks.
7. Calculate the average marks of all students.'''

class student:
    def __init__(self , roll_no , name , marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

'''Create an Employee class inside:

models/employee.py

ATTRIBUTES:

* employee_id
* name
* salary
* department

TASKS:

1. Take details of 5 employees from the user.
2. Create Employee objects.
3. Store the objects inside a list.
4. Display all employees.
5. Display employees whose salary is greater than 40,000.
6. Display employees who belong to the IT department.
7. Find the employee having the highest salary.
8. Calculate total salary of all employees.
9. Calculate average salary.'''

class employee:
    def __init__(self,employee,name,salary,department):
        self.emp = employee
        self.name = name
        self.salary = salary
        self.department = department

'''Create a Product class inside:

models/product.py

ATTRIBUTES:

* product_id
* product_name
* price
* quantity

TASKS:

1. Take details of 5 products from the user.
2. Create Product objects.
3. Store all objects in a list.
4. Display all products.
5. Calculate total value of each product.
   Total Value = Price × Quantity
6. Display products whose quantity is less than 10.
7. Find the product having the highest price.
8. Calculate total inventory value.
9. Search a product using Product Id.'''

class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quatity = quantity

'''Create an Account class inside:

models/account.py

ATTRIBUTES:

* account_no
* customer_name
* balance

METHODS:

* deposit()
* withdraw()
* display()

TASKS:

1. Create 5 Account objects.
2. Store all Account objects in a list.
3. Display all accounts.
4. Search an account using Account Number.
5. Deposit money into a selected account.
6. Withdraw money from a selected account.
7. Display accounts having balance greater than 50,000.
8. Find the account having the highest balance.'''

class account:
    def __init__(self,account,name,balance):
        self.acc_no = account
        self.name = name
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def diaplay(self):
        print("Account Number:",self.acc_no)
        print("Customer Name:",self.name)
        print("Account balance:",self.balance)

'''Create a Book class inside:

models/book.py

ATTRIBUTES:

* book_id
* book_name
* author
* price

TASKS:

1. Take details of 5 books from the user.
2. Create Book objects.
3. Store all Book objects in a list.
4. Display all books.
5. Search a book using Book Id.
6. Display all books written by a particular author.
7. Display books whose price is greater than 500.
8. Find the most expensive book.
9. Calculate average price of all books.'''

class book:
    def __init__(self,id,name,author,price):
        self.id = id
        self.name = name
        self.author = author
        self.price = price

'''Create a Customer class inside:

models/customer.py

ATTRIBUTES:

* customer_id
* customer_name
* city
* purchase_amount

TASKS:

1. Take details of 5 customers.
2. Create Customer objects.
3. Store all objects in a list.
4. Display all customers.
5. Display customers from a particular city.
6. Display customers whose purchase amount is greater than 10,000.
7. Find the customer having the highest purchase amount.
8. Calculate total sales.
9. Calculate average purchase amount.
10. Search customer using Customer Id.'''

class customer:
    def __init__(self,id,name,city,amount):
        self.id = id
        self.name = name
        self.city = city
        self.amount = amount

'''Create a Movie class inside:

models/movie.py

ATTRIBUTES:

* movie_id
* movie_name
* genre
* rating
* ticket_price

TASKS:

1. Take details of 5 movies from the user.
2. Create Movie objects.
3. Store all objects in a list.
4. Display all movies.
5. Display movies having rating greater than 8.
6. Display all Action movies.
7. Find the highest-rated movie.
8. Search a movie using Movie Id.
9. Calculate average movie rating.
10. Display movies whose ticket price is greater than 300.
'''

class movie:
    def __init__(self,id,name,genre,rating,price):
        self.id = id
        self.name = name
        self.genre = genre
        self.rate = rating
        self.price = price

