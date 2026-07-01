'''A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept'''

n = int(input("Enter a Number: "))

for i in range(1,len(str(n))) :
	m = str(n%10)
	s = str(n//10)
	if m in s :
		print("Not Valid.")
		break
else :
	print("Valid.")