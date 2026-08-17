'''Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.'''

N = int(input("Enter number of element: "))
lst = []
for i in range(N):
	lst.append(input("Enter Password: "))
PW = tuple(lst)

count = 0
for pas in PW :
	for word in PW :
		for i in range(len(pas)) :
			if pas[i] in word :
				break
		else :
			count +=1 
count = count/2
print(count)