'''Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zerosint
Work only on positive numbers
Then find leaders from the filtered sequence'''

n = int(input("Enter number of score:"))
l1 = map(int,input("Enter values").split())
f = []
for i in l1:
	if i > 0 :
		f.append(i)
if f:
	n = len(f)
	l = []
	s = 0
	for i in range(n):
		isleader = True
		for j in range(i+1,n):
			if f[i]<=f[j]:
				isleader = False
				break
		if isleader :
			l.append(f[i])
			s += f[i]
	print("Processing:")
	print("Filtered array:")
	print(f)
	print()
	print("Leaders:")
	print(l)
	print()
	print("Output:")
	print(s)
else :
	print(-1)



