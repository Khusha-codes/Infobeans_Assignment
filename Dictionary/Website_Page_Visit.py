'''A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.'''

pages = ["Home","About","Home","Contact","Home","About"]
d = {}

for x in pages:
	d[x] = d.get(x,0)+1

for k,v in d.items():
	print(k,"visited",k,"times")
