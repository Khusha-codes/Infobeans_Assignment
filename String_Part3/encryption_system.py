'''Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.'''

msg = input("Enter message: ")
temp = ""
word = ""

for ch in msg :
	if ch != " ":
		word += ch
	else :
		i = 1
		while i <= len(word) :
			temp += word[-i]
			i+=1
		else :
			temp += " "
			word = ""

i = 1
while i <= len(word) :
	temp += word[-i]
	i+=1

print(temp)
	