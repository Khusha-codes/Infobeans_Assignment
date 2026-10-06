"""
2. Employee Salary Report

A company stores employee salary information in employees.txt.

Each record contains:

EmployeeID,EmployeeName,Department,Salary
Task

Write a Python program to:

Accept employee details.
Store them in the file.
Read the file.
Display employees whose salary is greater than ₹50,000.
Calculate the average salary.
Sample Input
Enter number of employees: 4

"""

try:
    n = int(input("Enter number of Employee: "))
    with open("employee.txt","a") as f:
        for i in range(n):
            id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = int(input("Enter Salary: "))
            f.write(f"{id} {name} {department} {salary}\n")
    avg = 0
    print('''Employees with Salary > 50000
--------------------------------''')
    with open("employee.txt") as f:
        for line in f:
            l = line.strip().split()
            if int(l[3]) > 50000:
                print(f"{l[0]} {l[1]} {l[2]} {l[3]}")
            avg += int(l[3])
    print()
    print("Average Salary:",avg/n)
finally:
    print("ThankYou Have a nice day")