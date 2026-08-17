'''Prime Number Analyzer using List (Python)

Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them '''

n = int(input("Enter number of element: "))
num = []
for i in range(n):
	no = int(input("Enter number: "))
	num.append(no)
prime = []
nonprime = []
print("Prime Number: ",end = "")
for i in num :
	r = 2
	while r <= i/2 :
		if i%r == 0:
			nonprime.append(i)
			break
		r+=1
	else :
		print(i,end = " ")
		prime.append(i)
print()
print("Number of prime number",len(prime))
print("Number of non-prime number",len(nonprime))
new = sorted(prime)
print("Largest prime number is",new[-1])
print("All prime number are",prime)
print("Sorted prime number are",new)
