s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
	found = False
else:
	for i in s1:
		if s1.count(i) != s2.count(i) :
			break
	else:
		found = True
print(found)