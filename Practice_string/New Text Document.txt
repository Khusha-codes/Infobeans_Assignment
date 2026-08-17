S = input("Enter string: ")
for ch in S :
	if S.count(ch) > 1 :
		print("False")
		break
else :
	print("True")		