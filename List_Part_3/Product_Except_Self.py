'''For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result'''

n = int(input("enter number of element: "))
lst = []
for x in range(n):
	x = int(input("Enter value: "))
	lst.append(x)
result = []
for i in lst :
	prd = 1
	for j in lst :
		if j != i :
			prd = prd*j
	result.append(prd)
print("Result",result)