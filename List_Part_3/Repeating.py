'''A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message'''

N = int(input("Enter number of element: "))
lit = []
for i in range(N):
	x = int(input("Enter value: "))
	lit.append(x)
for n in lit :
	if n.count(n) != 1 :
	print("First Repeating Number =",n)
	break
else:
	print("No Repeating Number Found")