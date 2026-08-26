'''A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.'''

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
d = {}
for x in employee:
	d[x] = d.get(x,0)+1
print(d)

