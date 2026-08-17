'''Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.'''

ht = input("Enter hashtags: ").lower()
h1 = ht[0]
h2 = ht[1]

if ht.count(h1) < ht.count(h2):
	h1,h2 = h2,h1

for i in ht:
	if ht.count(i) >= ht.count(h1) :
		h1 = i
	elif ht.count(i) >= ht.count(h2):
		h2 = i

if h1 == h2 :
	print("no second highest frequency exists")
else :
	print("Second Trending Character is",h2)