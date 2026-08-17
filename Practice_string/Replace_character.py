s = input("Enter string: ")
ch = input("Enter character: ")
temp = ""
for i in s :
	if i == ch :
		temp += ch
	else :
		temp += i 
print(temp)
		