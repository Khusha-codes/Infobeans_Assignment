'''A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.'''

def al_eve(n):
	if n == 0 :
		return "Strong Password"
	if n%2 != 0:
		return "Weak Password"
	return al_eve(n//10)

n = int(input("Enter Password: "))
print(al_eve(n))