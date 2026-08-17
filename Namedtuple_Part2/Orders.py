'''An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.'''

from collections import namedtuple
order = namedtuple("ord",["order_id","customer_name","product_name","amount"])

n = int(input("Enter number of element: "))
cus_order =[]

for i in range(n):
	print("Enter details")
	id = int(input("Enter order id: "))
	name = input("Enter customer name: ")
	prd = input("Enter product name: ")
	amount = int(input("Enter amount: "))
	s = order(id,name,prd,amount)
	cus_order.append(s)

max = 0
sales = 0
amt = 0
for i in cus_order:
	if i.amount > 10000:
		amt +=1
	sales += i.amount
	if i.amount > max :
		max = i.amount
	print(*i)
print()

print("Order with highest amount: ")
for i in cus_order:
	if i.amount == max:
		print(*i)
print()

print("Total sales:",sales)
print()

print("Orders Above ₹10,000:")
print(atm)