'''Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list'''

n = int(input("Enter number of element: "))
l = []
for i in range(n) :
	ch = int(input("Enter number: "))
	l.append(ch)
P = []
c = 0
for i in l :
	if str(i) == str(i)[::-1] :
		P.append(i)
		c+=1
print("Palindromes:",P)
print("Count:",c)
p = sorted(P)
print("Lowest Palindrome is",p[-1])
print("Sorted:",p)