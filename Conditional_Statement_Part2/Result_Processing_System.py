'''A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail'''

marks = int(input("Enter marks: "))

if marks>90 :
	print("Grade : A")
elif marks>75 :
	print("Grade : B")
elif marks>60 :
	print("Grade : C")
elif marks>50 :
	print("Grade : D")
else :
	print("Fail")