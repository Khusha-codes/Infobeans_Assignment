'''STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit'''

dic = {}

def add(name,rollno,m1,m2,m3,m4,m5):
	lst = []
	lst.extend([m1,m2,m3,m4,m5])
	dic[rollno]["name"] = name
	dic[rollno]["marks"] = lst
	return "Student details added successfully."
	
def total(roll):
	for i in dic[roll]["marks"]:
		total += i
	return total

def per(roll):
	percentage = total(roll)
	percentage = percentage/5
	return percentage

def grade(roll):
	pctg = per(roll)
	if pctg >= 90:
		return "A+"
	elif pctg >= 80:
		return "A"
	elif pctg >= 70:
		return "B"
	elif pctg >= 60:
		return "C"
	elif pctg >= 50:
		return "D"
	else:
		return "Fail"

def hig(roll):
	h = dic[roll]["marks"][0]
	for x in dic[roll]["marks"]:
		if x > h:
			h = x
	return h

def low(roll):
	l = dic[roll]["marks"][0]
	for x in dic[roll]["marks"]:
		if x < l:
			l = x
	return l

def result(roll):
	print("----------- RESULT CARD -----------\n")
	print("Name	:",dic[roll]["name"])
	print("Roll Number:",roll)
	print()
	print("Marks")
	for x in range(len(dic[roll]["marks"])):
		print("Subject",x,":",dic[roll]["marks"][x])
	print()
	print("Total Marks:",total(roll))
	print("Percentage:",per(roll))
	print("Grade     :",grade(roll))
	print("Highest Mark:",hig(roll))
	print("Lowest Mark:",low(roll))

while True:
	print(" STUDENT RESULT MANAGEMENT \n")
	print('''1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit''')

	n = int(input("Enter choice: "))
	match n:
		case 1:
			name = input("Enter Student Name: ")
			roll = int(input("Enter Roll Number: "))
			print()
			m1 = int(input("Enter Mark 1: "))
			m2 = int(input("Enter Mark 2: "))
			m3 = int(input("Enter Mark 3: "))
			m4 = int(input("Enter Mark 4: "))
			m5 = int(input("Enter Mark 5: "))
			add(name,roll,m1,m2,m3,m4,m5)
		case 2:
			roll = int(input("Enter Roll Number: "))
			print("Total Marks =",total(roll))
		case 3:
			roll = int(input("Enter Roll Number: "))
			print("Percentage =",per(roll))
		case 4:
			roll = int(input("Enter Roll Number: "))
			print("Grade =",grade(roll))
		case 5:
			roll = int(input("Enter Roll Number: "))
			print(result(roll))
		case 6:
			roll = int(input("Enter Roll Number: "))
			print("Highest Mark =",hig(roll))
		case 7:
			roll = int(input("Enter Roll Number: "))
			print("Lowest Mark =",low(roll))
		case 8:
			print("Thank You. Program Terminated.")
			break
		case __:
			print("Wrong input please try again")
