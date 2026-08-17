'''A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.'''

from collections import namedtuple
student = nametuple("std",["roll_no","name","course","marks"])

n = int(input("Enter number of student: "))
students = []

for i in range(n):
	print("Enter details")
	r = int(input("Enter Roll No.: "))
	n = input("Enter Name: ")
	c = input("Enter Course: ")
	m = int(input("Enter Marks"))
	s = student(r,n,c,m)
	students.append(s)
print()

for i in students:
	print(*i)
print()

max = 0
avg = 0
count = 0
for i in students:
	avg += i.marks
	if i.marks > max:
		max = i.marks
	if i.marks > 80:
		count += 1
print("Topper of the class:")
for i in students:
	if i.marks == max:
		print(i.name)
print()

print(count,"Number of students scoring above 80 marks")
print()
avg = avg/n
print("average marks =",avg)
print()

c = input("Enter course: ")
print("students enrolled in that course:")
for i in students:
	if i.course == c:
		print(i.name)

print("")


