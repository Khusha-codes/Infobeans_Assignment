'''You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

n = int(input("Enter number of element in array: "))
a = []
result = []
for i in range(n):
	a.append(int(input("Enter element: ")))
print("Your array is:")
print(a)
fount = False
t = int(input("Enter target Number: "))

for i in range(n):
	for j in range(i+1,n):
		if a[i] + a[j] == t:
			result.append(i)
			result.append(j)
			fount = True
			print(result)
			break
	if fount:
		break
else :
	print("There is no such pair in array.")
