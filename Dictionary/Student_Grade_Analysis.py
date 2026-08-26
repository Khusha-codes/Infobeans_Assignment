'''Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.'''

students = {"Ajay":78,"Ravi":92,"Neha":85,"Aman":65}

hig = students[0][0]
low = students[0][0]

for k,v in students.items():
	if v < low :
		low = k
	elif v > hig :
		hig = k
print("Hightest Marks:",hig,students[hig])
print("Lowest Marks:",low,students[low])


