'''A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.'''

books = ["Python","Java","Python","C++","Java","Python"]
d = {}
for x in books:
	d[x] = d.get(x,0)+1
print(d)