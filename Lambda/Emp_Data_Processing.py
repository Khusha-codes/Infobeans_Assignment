'''Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
'''
def Second_hig(Age):
	age = list(Age)
	h1 = age[0]
	h2 = age[1]
	if h1 < h2:
		temp = h1
		h1 = h2
		h2 = temp
	for i in range(len(age)):
		if Age[i] > h1:
			h2 = h1
			h1 = age[i]
		elif Age[i] > h2 and age[i] != h1:
			h2 = age[i]
	if h1 == h2:
		return "No second highest value found"
	else :
		return h2

def Senior_Emp(Age):
	lst = list(filter(lambda x:x>50,Age))
	return len(lst)

def Duplicate(Age):
	lst = []
	for i in Age:
		if i not in lst:
			lst.append(i)
	return lst

def NSWV(str):
	word = ""
	count = 0
	for i in str:
		if i == " ":
			if word[0] in "aeiou":
				count+=1
			word = ""
		else:
			word += i
	return count

def Long_Name(str):
	name = ""
	temp = ""
	for i in str:
		if i == " ":
			if len(temp)> len(name):
				name = temp
			temp = ""
		temp += i
	return name
age = list(map(int,input("Employee Age: ").split()))
name = input("Employee Names: ")			
while True:
	print('''Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
''')

	n = int(input("Enter choice: "))
	match n:
		case 1:
			print(Second_hig(age))
		case 2:
			print(Senior_Emp(age))
		case 3:
			print(Duplicate(age))
		case 4:
			print(NSWV(name))
		case 5:
			print(Long_Name(name))
		case 6:
			break
		case __:
			print("invalide input")

