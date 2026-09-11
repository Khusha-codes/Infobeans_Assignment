import NUMBER_ANALYSIS_SYSTEM as num
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
			print(num,perfect(n))
		case 2:
			print(num.palindrome(n))
		case 3:
			print(num.strong(n))
		case 4:
			print(num.arm(n))
		case 5:
			print(num.prime(n))
		case 6:
			print(num.eve_odd(n))
		case 7:
			print(num.factorial(n))
		case 8:
			print(num.digit_sum(n))
		case 9:
			print(num.rev(n))
		case 10:
			print(num.no_digit(n))
		case 11:
			print(num.automorphic(n))
		case 12:
			print(num.neon(n))
		case 13:
			print(num.spy(n))
		case 14:
			print(num.harshad(n))
		case 15:
			print("Thanks for using Number Analysis System")
			break
		case __:
			print("Try again")