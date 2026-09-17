'''A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.
'''

class Employee:
    def __init__(self,id,name,bs):
        self.id = id
        self.name = name
        self.bs = bs

    def calulationss(self):
        self.hra = (self.bs*2)/10
        self.da = (self*15)/100
        self.salary = self.bs + self.hra + self.da

    def display(self):
        print("Employee ID      :",self.id)
        print("Employee Name    :",self.name)
        print("Basic Salary     :",self.bs)
        print("HRA              :",self.hra)
        print("DA               :",self.da)
        print("Gross Salary     :",self.salary)

id = int(input("Enter Employee ID : "))
name = input("Enter Employee Name : ")
bs = int(input("Enter Basic Salary :"))

emp = Employee(id,name,bs)
emp.calulationss
emp.displya