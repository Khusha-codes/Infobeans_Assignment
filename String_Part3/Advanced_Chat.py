'''Advanced Smart Chat Compression Expansion System

A messaging application stores repeated characters in compressed form to
reduce storage space. Before displaying messages to users, the system
should reconstruct the original message.

The application team has introduced additional rules.

Conditions: - Alphabet followed by number - Repeat character according
to the number - If alphabet is uppercase convert expanded characters
into lowercase - Ignore special symbols - Display expanded string -
Display total character count'''

msg = input("Enter compressed message: ").lower()

alpha = ""
num = 0
total = 0

for ch in msg :
	if ch.isalpha() :
		alpha = ch
	elif ch.isdigit() :
		num = int(ch)
		print(alpha*num , end = "")
	total += 1

print()
print("Total Characters:",total)