S = input("Enter string: ")
word = input("Enter word: ")
if word in S:
	print(S.count(word))
else :
	print("Word not found")