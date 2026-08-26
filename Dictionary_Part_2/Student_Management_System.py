'''ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit''''

student = {
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}

while True:
	print("Menu\n")
	print('''=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit''')

	n = int(input("Enter choice: "))

	match n:
		case 1:
			id = int(input("Enter Student ID: "))
			name = input("Enter Student Name: ")
			course = input("Enter Course Name: ")
			number = int(input("Enter Mobile Number: "))
			fees = int(input("Enter Fees: "))
			city = input("Enter City: ")
			student[id] = {"name":name,
"course":course,
"phone":number,
"fees":fees,
"city",city
}

		case 2:
			if id in student:
				id = int(input("Enter Student ID: "))
				for k,v in student[id].items():
					print(k," : ",v)
			else:
				print("Student Not Found")
		case 3:
			id = int(input("Enter Student ID: "))
			if id in student:
				course = input("Enter Course Mame: ")
				student[id][course] = course
				print("Course Updated Successfully") 
			else:
				print("Student Not Found")
		case 4:
			id = int(input("Enter Student ID: "))
			if id in student:
				del student[id]
				print("Student Deleted Successfully") 
			else:
				print("Student Not Found")
		case 5:
			for key,value in student.items:
				print("-----------------------------------")
				for k,v in value.items():
					print(k," : ",v)
				print("-----------------------------------")
		case 6:
			count = 0
			for i in student:
				count += 1
			print("Total Students : "count)
		case 7:
			course = input("Enter Course Name: ")
			for key,value in student:
				if value["course"] == course :
					print(value["id"]," ",value["name"])
		case 8:
			city = input("Enter City Name: ")
			for key,value in student:
				if value["city"] == city :
					print(value["id"]," ",value["name"])
		case 9:
			print("Highest Fee Paying Student")
			max = 0
			for k,v in student.items():
				if v["fees"] > max:
					max = k
			for k,v in student[max].items():
				print(k," : ",v)
		case 10:
			print("Lowest Fee Paying Student")
			min = 0
			for k,v in student.items():
				if v["fees"] > min:
					min = k
			for k,v in student[min].items():
				print(k," : ",v)
		case 11:
			print("Thank You For Using Student Management System")
			break
		case __:
			print("Try again!!!")