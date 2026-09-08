s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) != len(s2):
	print("False")
else:
	i=0
	while i < len(s1):
		if s1[i] != s2[i]:
			print("False")
			break
		i+=1
	else:
		print("True")