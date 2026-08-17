''' Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report*
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*'''

n = int(input("Number of student: "))
A = []
B = []
C = []
F = []
Sa=Sb=Sc=Sf = 0
for i in range(n):
	no = int(input("Enter number: "))
	if no >= 90 :
		A.append(no)
		Sa += 1
	elif no >= 75 :
		B.append(no)
		Sb += 1
	elif no >= 55 :
		C.append(no)
		Sc += 1
	else:
		F.append(no)
		Sf += 1
S = Sa + Sb + Sc + Sf

print("\n===== STUDENT GRADE REPORT =====\n")
print("A Grade Students   :",A)
print("B Grade Students   :",B)
print("A Grade Students   :",C)
print("Fail Students      :",F)
print("\n--------------------------------")
print("A Count   :",Sa)
print("B Count   :",Sb)
print("C Count   :",Sc)
print("Fail Count:",Sf)
print("--------------------------------\n")
print("Total Students:",S)