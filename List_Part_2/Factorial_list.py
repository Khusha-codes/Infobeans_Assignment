'''Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even'''

l = map(int,input("Enter element of array: ").split())
f = []
c = 0
for i in l :
	if i > 0 :
		j = m = 1
		while j <= i :
			m = m*j
			j+=1
		if m%2 == 0 :
			c+=1
		f.append(m)
		m = 1
print(f)
print("Sum = ",sum(f))
print("Max",max(f))
print("Even Count =",c)
