'''A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

Task

Write a recursive function to determine whether a given digit is present.'''

def det(n,k):
	if n == 0:
		return "Digit  Not Found"
	if n%10 == k:
		return "Digit Found"
	return det(n//10,k)

n = int(input("Enter Patient ID: "))
k = int(input("Enter Digit: "))

print(det(n,k))
