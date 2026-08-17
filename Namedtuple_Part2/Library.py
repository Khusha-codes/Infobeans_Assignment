'''A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.'''

from collections import namedtuple
book = namedtuple("lib",["book_id","title","author","price"])

n = int(input("Enter number of books: "))
books =[]

for i in range(n):
	print("Enter details")
	id = int(input("Enter book id: "))
	tt = input("Enter book title: ")
	atr = input("Enter author name: ")
	amount = int(input("Enter book price: "))
	s = order(id,tt,str,amount)
	books.append(s)

max = 0
avg = 0
for i in books:
	print(*i)
	avg += i.price
	if max < i.price :
		max = i.price
print()

print("Most expensive book: ")
for i in books:
	if max == i.price:
		print(i.title)
print()

atr = input("Enter author name: ")
for i in books:
	if atr == i.author :
		print(*i)

avg = avg/n
print("Average price of all books:")
print(avg)