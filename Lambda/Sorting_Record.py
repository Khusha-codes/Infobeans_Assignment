'''Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.
'''
n = int(input("Enter number of element: "))
d = []
for i in range(n):
	k = input("Enter key: ")
	v = input("Enter value: ")
	a = (k,v)
	d.append((k,v))
print(sorted(d,key = lambda x:x[1]))
	