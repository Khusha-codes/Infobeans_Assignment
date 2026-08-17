'''Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message'''

N = int(input("Enter number of element: "))
lst = []
for n in range(N) :
	x = int(input("Enter value: "))
	lst.append(x)
sumr = 0
suml = 0
for n in range(N) :
	for x in range(n) :
		sumr += lst[x]
	for y in range(n+1,N) :
		suml += lst[y]
	if sumr == suml :
		print("Equilibrium Index =",n)
	sumr = 0
	suml = 0

	