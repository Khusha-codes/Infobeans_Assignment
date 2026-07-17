'''Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.'''

msg = input("Enter chat message:").lower()
count = 0

for i in msg :
	if i == " ":
		count += 1

print("Total Spaces:",count)