'''Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.'''

msg = input("Enter message: ")
temp = ""

i = 0
while i < len(msg) :
	temp += msg[i]
	if msg[i] == " " :
		while msg[i] == " " :
			i+=1
	else :
		i+=1

print("Cleaned Message:",temp)