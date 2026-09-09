'''A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.'''

def fib(x,p=0,n=1):
	s = p+n
	if x == 2:
		print(count)
		return count
	else:
		count.append(s)
		print(s)
		q = n
		m = s
		fib(x-1,q,m)

count = [0,1]
n = int(input("Enter number: "))

print(fib(n))
#print(reduce(lambda x,y:x+y , range(n)))