'''A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.'''

# Using for loop

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
count = 1

for i in range(n1,n2+1) :
	if i%7 == 0 :
		count +=1

print("Output: ",count)

# Using for loop

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
count = 1
i = 1

while n1 <= n2:
	if i%2 == 0 :
		count +=1
	n1+=1

print("Output: ",count) 