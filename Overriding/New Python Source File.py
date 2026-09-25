'''Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager


Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.'''

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        print("Kirti is kirti")

class Developer(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)

    def calculate_bonus(self):
            print("Bonus :",self.salary/10)

class Manager(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)

    def calculate_bonus(self):
            print("Bonus :",self.salary/5)

id = int(input("Employee ID : "))
name = input("Employee Name : ")
salary = int(input("Enter Salary: "))
type = input("Enter Employee Type: ").lower()

if type == "developer":
     obj = Developer(id,name,salary)
     obj.calculate_bonus()
elif type == "manager":
     obj = Manager(id,name,salary)
     obj.calculate_bonus()
else:
     print("Wrong Employee Type")
