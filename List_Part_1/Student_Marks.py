'''Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75'''

n = int(input("Enter number of student: "))
M = []
for i in range(n) :
	ch = int(input("Enter marks: "))
	M.append(ch)
h = M[0]
l = M[0]
c = 0
for i in M :
	if i > h :
		h = i
	if i < l :
		l = i
	if i > 75 :
		c += 1
print("Marks are",M)
print("Highest marks is",h)
print("Lowest marks is",l)
print("Number of marks above 75 are",c)