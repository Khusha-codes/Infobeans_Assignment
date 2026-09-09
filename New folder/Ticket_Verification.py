'''A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.'''

def digit(n,k,c=0):
	if n%10 == k:
		c += 1
	if n == 0:
		return c
	return digit(n//10,k,c)

n = int(input("Enter Ticket Number: "))
k = int(input("Enter Lucky Digit: "))
c = digit(n,k)
print("Digit",k,"appears",c,"times")