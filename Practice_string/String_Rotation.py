s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
	found = False
else:
	temp = s1*2
	print(s2 in temp)
	'''for i in range(len(temp)):
		if temp[i] == s2[0]:
			k = 0
			while k < len(s2):
				if temp[i+k] != s2[k]:
					break
				k+=1
			else:
				found = True
		if found:
			break
print(found)'''