'''Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.'''

n = int(input("Enter number of element: "))
lst = []

for I in range(n):
	lst.append(int(input("Enter element: ")))

m1 = lst[0]
for I in lst:
	if m1 < I :
		m1 = I 

i = 0
while i < len(lst):
	if m1 == lst[i]:
		lst.pop(i)
		i = -1
	i+=1

if lst:
	m2 = lst[0]
	for I in lst:
		if m2 < I :
			m2 = I 

i = 0
while i < len(lst):
	if m2 == lst[i]:
		lst.pop(i)
		i = -1
	i+=1

if lst:
	m3 = lst[0]
	for I in lst:
		if m3 < I :
			m3 = I 

if lst:
	print(m3)
else: 
	print(m1)