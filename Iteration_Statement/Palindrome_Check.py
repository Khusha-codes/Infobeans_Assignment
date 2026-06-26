'''A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.'''

# using for loop

n = int(input("Enter a number : "))
temp = n
reverse = 0

for i in range(len(str(temp))):
	reverse = reverse*10 + temp%10
	temp = temp//10

if reverse == n :
	print("Palindrome.")
else :
	print("Not a Palindrome.")

# using while loop 

n = int(input("Enter a number : "))
temp = n
reverse = 0

while temp != 0 :
	reverse = reverse*10 + temp%10
	temp = temp//10

if reverse == n :
	print("Palindrome.")
else :
	print("Not a Palindrome.")

