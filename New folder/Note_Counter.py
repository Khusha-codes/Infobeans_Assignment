'''A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop'''

n = int(input("Enter Number: "))
sum = 0

while n >= 100 :
	sum+=1
	n = n - 100

print("Notes =",sum)