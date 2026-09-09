'''A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.'''

from functools import reduce
students = input("Enter Student name: ").split()

name = reduce(lambda x,y: x if len(x)>len(y) else y,students)

print("Student with the longest name:",name)