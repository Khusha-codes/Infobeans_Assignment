'''An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.'''

cla = int(input("Enter number of classes: "))
std = int(input("Enter students per class: "))
sub = int(input("Enter subjects per student: "))

for k in range(cla) :
	print("Class ",k+1)
	for j in range(std) :
		print("Student ",j+1)
		sum = 0
		for l in range(sub) :
			print("")
			n = int(input("Enter mark:"))
			print("")
			sum = sum + n
		print("Class ",k+1)
		print("Student",j+1,"Total =",sum)