'''Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.'''

code = input("Enter Product Code: ")

for i in range(len(code)//2) :
	if code[i] != code[-(i+1)] :
		print("Not a Palindrome Code")
		break
else :
	print("Palindrome Code")