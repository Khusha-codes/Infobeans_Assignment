'''6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.'''

fb = input("Enter your Feedback: ").split()
wd = input("Enter Word: ")
count = 0
 
for ch in fb :
	if ch == wd :
		count+=1
print(count,"times word",wd,"appears in a review.")


