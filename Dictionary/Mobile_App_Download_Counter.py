'''Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.'''

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
d = {}
for x in cities:
	d[x] = d.get(x,0)+1
most = d[0]
for k,v in d.items():
	if v > d[most]:
		d = k
print(d)
print("Most Downlaods:",most)