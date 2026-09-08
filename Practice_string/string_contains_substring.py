s1 = input("Enter string: ")
s2 = input("Enter sub-string: ")

found = False
for i in range(len(s1)):
	if s1[i] == s2[0]:
		j = i
		k = 0
		while k < len(s2):
			if s1[j] != s2[k]:
				break
			j+=1
			k+=1
		else :
			found = True

print(found)