'''A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.'''

# Using for loop

n = int(input("Enter Number: "))
temp = n
sum = 0

for i in range(1,len(str(n))) :
	sum += temp%10
	temp//10

if n%sum == 0 :
	print("Strong Number.")
else :
	print("Not a Strong Number.")


# Using for loop

n = int(input("Enter Number: "))
temp = n
sum = 0

while temp >0 :
	sum += temp%10
	temp//10

if n%sum == 0 :
	print("Strong Number.")
else :
	print("Not a Strong Number.")
 