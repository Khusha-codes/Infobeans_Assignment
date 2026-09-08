s = input("Enter string: ")
word = ""
result = ""

for i in s:
	if i == " ": 
		result = result + " " + word[::-1]
		word = ""
	else:
		word += i
result = result + " " + word[::-1]
print(result)