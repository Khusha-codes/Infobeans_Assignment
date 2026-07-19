'''Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity'''

first = input("Enter first product code: ").lower()
second = input("Enter Second product code: ").lower() 

l1 = len(first)
l2 = len(second)
first = sorted(first)
second = sorted(second)

s1 = ""
s2 = ""

for ch in first :
	if ch.isalnum() :
		s1 += ch 
for ch in second :
	if ch.isalnum() :
		s2 += ch
if s1 == s2 :
	print("Both Product Codes are Matching")
else :
	print("Both Product Codes are not Matching")