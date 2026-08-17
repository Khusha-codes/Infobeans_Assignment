S = input("Enter string: ").lower()
ch = input("Enter character: ").lower()
for i in range(len(S)):
	if S[i] == ch :
		print(i)
		break
