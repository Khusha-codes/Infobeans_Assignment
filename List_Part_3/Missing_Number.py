'''Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1'''

N = int(input("Enter number of value: "))
lst = []
for i in range(N):
	x = int(input("Enter value: "))
	lst.append(x)
for i in range(1,N+1):
	if i != lst[i-1]:
		print("Missing Number =",i)
		break
else :
	print("No Missing Number")