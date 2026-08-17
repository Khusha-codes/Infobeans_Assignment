'''A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order'''

N = int(input("Enter number of element: "))
lst = []
d = []
count = 0
for n in range(N) :
	x = int(input("Enter element: "))
	lst.append(x)
for m in lst :
	if lst.count(m) > 1 :
		d.append(m)
		count += 1
if d :
	print("Duplicate Numbers =",d)
	print("Count =".count)
else :
	print("No Duplicate Numbers Found")