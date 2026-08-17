'''Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message'''

N = int(input("Enter number of element: "))
lst = []
for i in range(N):
	x = int(input("Enter element: "))
	lst.append(x)
Max = 0
for n in lst :
	if N//2 < lst.count(n) :
		Max = n
if Max :
	print("Majority Element =",Max)
else :
	print("No Majority Element Found")
