s = input("Enter string: ")
w = input("Enter word: ")
word = ""
result = ""
i = 0
while i <len(s):
	for j in range(i,len(s)):
		if s[j] == " ":
			if word == w :
				print(i,end=" ")
			word = ""
		word += j
	i = j