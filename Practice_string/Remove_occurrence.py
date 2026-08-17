S = intput("Enter string: ")
ch = input("Enter character: ")
for i in S :
	if i == ch :
		S.remove(i)
print(S)