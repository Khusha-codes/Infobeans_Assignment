'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.'''

n1 = int(input("Enter number of element for 1st list: "))
num1 = []

for i in range(n1):
	num1.append(int(input("Enter elemenet of 1st list: ")))

n2 = int(input("Enter number of element in 2nd list: "))
num2 = []

for i in range(n2):
	num2.append(int(input("Enter element of 2nd list: ")))

r1 = []

for i in num1:
	if i not in num2:
		if i not in r1 :
			r1.append(i)

r2 = []

for i in num2:
	if i not in num1:
		if i not in r2 :
			r2.append(i)

result = [r1, r2]

print(result)