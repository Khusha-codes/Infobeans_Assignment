'''Frequency Count of Elements (Advanced Scenario-Based Problem)


A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

The department wants to analyze:

* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)

---

 Requirements

Write a Python program to:

1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary'''

n = int(input("Enter number of survey"))
l = []
for i in range(n):
	r = int(input("Enter number: "))
	if r > 0 :
		l.append(r)
mf = str(l.count(l[0]))
lf = str(l.count(l[0]))
print("Frequency Count:")
for i in l :
	print(i,"-->",l.count(i))
	if l.count(i) > mf :
		mf = str(i)
	elif l.count(i) == mf :
		mf = mf + " or " + str(i)
	if l.count(i) < lf :
		lf = str(i)
	elif l.count(i) == lf :
		lf = lf + " or " + str(i)
print()
print("Most Frequent:",mf)
print("Least Frequent:",lf)





