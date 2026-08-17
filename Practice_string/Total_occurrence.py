S = input("Enter string: ").lower()
ch = input("Enter character: ").lower()
sum = 0
for i in range(len(S)):
	if S[i] == ch :
		sum += 1
print(sum)
