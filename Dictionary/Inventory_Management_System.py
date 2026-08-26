'''Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

stock = {"Pen":50,"Pencil":100,"Eraser":25,"Marker":10}

for k,v in stock:
	if v < 30 :
		print(k)