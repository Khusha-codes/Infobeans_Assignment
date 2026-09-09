'''A file compression company wants to reduce the size of text files before storing them. One simple compression technique is to replace consecutive repeated characters with the character followed by its count.

For example:

AAABBCCCCD → A3B2C4D1

As a software developer, your task is to write a recursive Python program to compress a given string.

Task

Write a recursive function that compresses a string by counting consecutive occurrences of each character.
'''
def compress(st,c=0):
	c+=1
	if len(st) == 1:
		return st + str(c)
	if st[-1] != st[-2]:
		s = st[0:len(st)-1]
		return compress(s,c=0) + st[-1] + str(c)
	s = st[0:len(st)-1]
	return compress(s,c)

n = input("Enter a String: ")
print(compress(n))