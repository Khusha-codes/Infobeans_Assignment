'''orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.'''

orders = ["Pizza","Burger","Pizza","Pasta","Burger","Pizza","Pasta"]
d = {}
for x in orders:
	d[x] = d.get(x,0)+1
most = d[0]
for k,v in d:
	if v > most:
		most = k
	print(k,":",v)
print("Most Ordered :",most)