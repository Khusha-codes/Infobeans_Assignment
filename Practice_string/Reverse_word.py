s = input("Enter string: ")
word = ""
result = ''
for i in s:
	if i == " ":
		result = word + " " + result
		word = ""
	else :
		word += i
result = word + " " + result
print(result)