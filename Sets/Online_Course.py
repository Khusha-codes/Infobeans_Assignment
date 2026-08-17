'''An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit'''

while true :
	print('''
Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit
''')

	n = int(input("Enter your Choice: "))
	print()
	P = set()
	J = set()

	match n:
		case 1:
			no = int(input("Enter number of student: "))
			print()
			lst = []
			for i in no :
				lst.append(input("Enter student name: "))
			P.update(lst)
			print()
		case 2:
			no = int(input("Enter number of student: "))
			print()
			lst = []
			for i in no :
				lst.append(input("Enter student name: "))
			J.update(lst)
			print()
		case 3:
			for i in P:
				print(i)
			print()
		case 4:
			for i in J:
				print(i)	
			print()
		case 5:
			print("Students in Both Cource: ")
			print(P|J)
			print()
		case 6:
			print("Students Enrolled Only in Python")
			print(P-J)
			print()
		case 7:
			print("Students Enrolled Only in Java")
			print(J-P)
			print()
		case 8:
			name = input("Enter name of student: ")
			print(name in P)
			print()
		case 9:
			print("Total Unique Club Members")
			print(len(P^J))
			print()
		case 10:
			break
		case __:
			print("Try Again")
			print()