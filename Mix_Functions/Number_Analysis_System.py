'''Create a Menu-Driven Number Analysis System in Python.

The program should continuously display a menu and allow the user to select different operations related to numbers.

Each operation must be implemented using a separate function.

The program should continue running until the user selects Exit.

Main Menu

When the program starts, display:

========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit'''

def perfect(x,y=1,count=0):
	if x%y == 0:
		count += y
	if y > x/2:
		if count == x:
			return "Perfect Number"
		else:
			return "Not a Perfect Number"
	return perfect(x,y+1,count)

def palindrome(x):
	m = str(x)
	w = m[::-1]
	if m == w :
		return "Palindrome Number"
	return "Not a Palindrom Number"	

def arm(n):
	m = n
	l = len(str(n))
	sum = 0
	while m > 0:
		sum += (m%10)**l
		m = m//2
	if sum == n:
		return "Strong Number"
	else:
		return "Strong Number"

def prime(n):
	i = 2
	while i < n//2:
		if n%i == 0:
			return "Not a Prime Number"
		i += 1
	return "Pirme Number"

def eve_odd(n):
	if n%2 == 0 :
		return "Even Number"
	return "Odd Number"

def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)

def strong(x):
	m = x
	result = 0
	while m > 0:
		p = m%10
		result = result + factorial(p)
		m = m//10
	if result == x:
		return "Strong Number"
	return "Not a Strong Number"

def digit_sum(n,s=0):
	if n == 0 :
		return s
	s += n%10 
	return digit_sum(n//10,s)

def rev(n,r=0):
	if n == 0 :
		return r
	r = r*10 + n%10
	return rev(n//10,r)

def no_digit(n,c=0):
	if n == 0 :
		return c
	c += 1
	return no_digit(n//10,c)

def automorphic(n):
	s = n*n
	if str(n) in str(s):
		return "Automorphic Number"
	else:
		return "Not a Automorphic Number"

def neon(n):
	s = n*n
	d = digit_sum(s)
	if d == n:
		return "Neon Number"
	return "Not Neon Number"

def spy(n):
	d = digit_sum(n)
	p = 1
	while n > 0:
		p = p*(n%10)
		n = n//10
	if p == d:
		return "Spy Number"
	return "Not a Spy Number"

def harshad(n):
	d = digit_sum(n)
	if n%d == 0:
		return "Harshad Number"
	return "Not a Harshad Number"

while True:
	print('''========================================
       NUMBER ANALYSIS SYSTEM
========================================

1. Check Perfect Number
2. Check Palindrome Number
3. Check Strong Number
4. Check Armstrong Number
5. Check Prime Number
6. Check Even or Odd
7. Find Factorial
8. Find Sum of Digits
9. Reverse a Number
10. Find Number of Digits
11. Check Automorphic Number
12. Check Neon Number
13. Check Spy Number
14. Check Harshad Number
15. Exit\n''')
	
	c = int(input("Enter choice: "))
	n = int(input("Enter Number: "))
	match c:
		case 1:
			print(perfect(n))
		case 2:
			print(palindrome(n))
		case 3:
			print(strong(n))
		case 4:
			print(arm(n))
		case 5:
			print(prime(n))
		case 6:
			print(eve_odd(n))
		case 7:
			print(factorial(n))
		case 8:
			print(digit_sum(n))
		case 9:
			print(rev(n))
		case 10:
			print(no_digit(n))
		case 11:
			print(automorphic(n))
		case 12:
			print(neon(n))
		case 13:
			print(spy(n))
		case 14:
			print(harshad(n))
		case 15:
			print("Thanks for using Number Analysis System")
			break
		case __:
			print("Try again")