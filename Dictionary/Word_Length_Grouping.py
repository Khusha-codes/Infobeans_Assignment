'''A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.'''

tags = ["python","java","api","react","html","css"]
d = {}

for x in tags:
	l = len(x)
	if l not in d:
		d[l] = []
	d[l].append(x)
print(d)