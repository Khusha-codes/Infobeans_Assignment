'''NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
'''
def perfect(n):
	s = 0
	for i in n//2:
		if n%1 == 0:
			s += i
	if s == n:
		return "Perfect Number"
	else:
		return "Not Perfect Number"


def prime(n):
	if n < 2:
		return "Not Prime Number"
	for i in range(2,n//2):
		if n%i == 0:
			return "Not Prime Number"
		else :
			return "Prime Number"

def rev(n):
	r = 0
	temp = n
	while temp > 0:
		r = r*10 + temp%10
		temp = temp//10
	return r

def fac(n):
	f = 1
	for i in range(1,n+1):
		f = f*i
	return f

def dis(n):
	fac = ""
	for i in range(n+1):
		if n%i == 0:
			fac = fac + str(i) + " "
	return fac

while True:
	print('''MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit
\n''')
	n = int(input("Enter Choice: "))
	print()
	match n:
		case 1:
			n = int(input("Enter Number: "))
			print(perfect(n))
		case 2:
			n = int(input("Enter Number: "))
			print(prime(n))
		case 3:
			n = int(input("Enter Number: "))
			print(rev(n))
		case 4:
			n = int(input("Enter Number: "))
			print(fac(n))
		case 5:
			n = int(input("Enter Number: "))
			print(dis(n))
		case 6:
			print("Thanks for using Number System")
			break
		case __:
			print("Invalid Choice Try Again")
	