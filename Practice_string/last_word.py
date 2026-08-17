S = input("Enter string: ")
word = input("Enter word: ")
if word in S:
	print(S.rfind(word))
else :
	print("Word not found")