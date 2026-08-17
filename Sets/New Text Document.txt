'''A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit'''

while true :
	print('''
Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit
''')

	n = int(input("Enter your Choice: "))
	print()
	C_club = set()
	R_club = set()

	match n:
		case 1:
			no = int(input("Enter number of student: "))
			print()
			lst = []
			for i in no :
				lst.append(input("Enter student name: "))
			C_club.update(lst)
			print()
		case 2:
			no = int(input("Enter number of student: "))
			print()
			lst = []
			for i in no :
				lst.append(input("Enter student name: "))
			C_club.update(lst)
			print()
		case 3:
			for i in C_club:
				print(i)
			print()
		case 4:
			for i in R_club:
				print(i)	
			print()
		case 5:
			print("Students in Both Clubs: ")
			print(C_club|R_club)
			print()
		case 6:
			print("Students Only in Coding Club:")
			print(C_club-R_club)
			print()
		case 7:
			print("Students Only in Robotics Club")
			print(R_club-C_club)
			print()
		case 8:
			print("All Unique Club Members")
			print(C_club^R_club)
			print()
		case 9:
			print("Total Unique Club Members")
			print(len(C_club^R_club))
			print()
		case 10:
			break
		case __:
			print("Try Again")
			print()