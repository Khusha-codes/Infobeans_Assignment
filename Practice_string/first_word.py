s = input("Enter string: ")
word = input("Enter string: ")
if word in s:
	print(s.find(word))
else:
	print("Word not found")