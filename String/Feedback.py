'''Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.'''

feedback = input("Enter feedback message:").lower()
count = 0

for i in feedback :
	if i in "aeiou":
		count += 1

print("Total vowels:",count)