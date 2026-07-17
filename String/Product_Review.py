'''Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.'''

msg = input("Enter chat message:").lower()
check = input("Enter character to check:").lower()
count = 0

for i in msg :
	if i == check:
		count += 1

print("Character '",check,"' occurs:",count,"times")