'''Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.'''

sms = input("Enter SMS: ").split()
shortest = sms[0]

for i in range(len(sms)) :
	temp = sms[i]
	if len(temp) < len(shortest) :
		shortest = temp
print("Shortest word from the given SMS is",shortest)