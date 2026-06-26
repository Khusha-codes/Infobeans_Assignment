'''A security system stores OTP codes in reverse format for encryption to increase data safety. Reversing a number means extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.'''

# using for loop

n = int(input("Enter a number : "))
temp = n
reverse = 0

for i in range(len(str(temp))):
	reverse = reverse*10 + temp%10
	temp = temp//10

print(reverse)

# using while loop 

n = int(input("Enter a number : "))
temp = n
reverse = 0

while temp != 0 :
	reverse = reverse*10 + temp%10
	temp = temp//10

print(reverse)