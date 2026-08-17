'''A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.'''

from collections import namedtuple
emp = namedtuple("employee",["emp_name","department","salary"])

n = int(input("Enter number of employees: "))
lst = []

for i in range(n) :
	print("Enter details")
	name = input("Enter name: ")
	dprt = input("Enter department name: ")
	salary = int(input("Enter salary: "))
	lst.append(emp(name,dprt,salary))

for i in lst:
	print(i)

d = input("Enter department: ")

hs = lst[0].salary
ls = lst[0].salary
avg = 0
for i in lst :
	if hs < i.salary :
		hs = i.salary
	if ls > i.salary :
		ls = i.salary
	avg += i.salary
avg = avg/n

print("Highest Salary Employee: ")
for i in lst :
	if hs == i.salary :
		print(*i)

print("Lowest Salary Employee: ")
for i in lst :
	if ls == i.salary :
		print(*i)

print("Average Salary:")
print(avg)

print("Employees in",d,"Department:")
for i in lst :
	if i.department == d :
		print(i)


