'''An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.'''

from collections import namedtuple
product = namedtuple("pdt",["product_id","product_name","price"])

n = int(input("Enter number of products: "))

lst = []
for i in range(n):
	print("Enter details")
	id = input("Enter product id: ")
	name = input("Enter product name: ")
	price = int(input("Enter product price: "))
	s = product(id,name,price)
	lst.append(s)
print()

max = 0
cheap = lst[0.price]
avg = 0
print("All Products:")
for i in lst:
	avg = i.price
	if max < i.price :
		max == i.price
	if cheap > i.price :
		cheap == i.price
	print(*i)
print()

print("Costliest Product:")
for i in lst:
	if i.price == max:
		print(*i)
printt()

print("Cheapest Product:")
for i in lst:
	if i.price == cheap:
		print(*i)
print()

print("Average Price:")
avg = avg/n
print(avg)
print()

print("Products Above ₹50,000:")
for i in lst:
	if i.price > 50000:
		print(*i)

