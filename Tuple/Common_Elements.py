'''Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.'''

n1 = int(input("Enter number of element in 1st array: "))
A = []
for i in n1 :
	A.append(int,input("Enter element of 1st array: "))
n2 = int(input("Enter number of element in 2nd array: "))
B = []
for i in n2 :
	B.append(int,input("Enter element of 2st array: "))
n3 = int(input("Enter number of element in 3nd array: "))
C = []
for i in n3 :
	C.append(int,input("Enter element of 3st array: "))

hcf = []

for i in A :
	if i in B :
		if i in B :
			hcf.append(i)
if hcf :
	print("Common elements are",hcf)
else :
	print("No common elements")
