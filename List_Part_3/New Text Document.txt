'''An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message'''

N = int(input("Enter number of element: "))
lit = []
for i in range(N):
	x = int(input("Enter value: "))
	lit.append(x)
for n in lit :
	if n.count(n) == 1 :
	print("First Non-Repeating Number =",n)
	break
else:
	print("No Non-Repeating Number Found")