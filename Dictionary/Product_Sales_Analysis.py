'''sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.'''

sales = ["Mobile","Laptop","Mobile","Tablet","Laptop","Mobile"]
d = {}
for x in sales:
	d[x] = d.get(x,0)+1
for k,v in d:
	print(k, ":", v)
