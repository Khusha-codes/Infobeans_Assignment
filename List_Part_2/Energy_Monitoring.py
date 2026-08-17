'''Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1'''

arr = []
p = []
ss = 0
s = 0
n = int(input("Enter size: "))

for i in range(n):
	c = int(input("Enter energy: "))
	arr.append(c)	
for i in range(n):
	if i == 0 :
		if n==1 or arr[i] >= arr[i+1]:
			p.append(arr[i])
			ss += arr[i]**2
			s += arr[i]
	elif i == n-1 :
		if arr[i] >= arr[i-1]:
			p.append(arr[i])
			ss += arr[i]**2
			s += arr[i]
	else:
		if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
			p.append(arr[i])
			ss += arr[i]**2
			s += arr[i]
avg = s/len(p)
s = sorted(p)
d = s[-1] - s[0]
if p :
	print("Peaks:",p)
	print("Sum of squares",ss)
	print("Average",avg)
	print("Difference",d)
else:
	print("Peak not found")

