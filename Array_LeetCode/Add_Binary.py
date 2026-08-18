'''Given two binary
 strings a and b, return their sum as a binary string.'''

a = int(input("Enter first str: "))
b = int(input("Enter second str: "))

b1 = 0
i = 0
while a > 0:
	b1 = b1 + ((a%10)*(2**i))
	a = a//10
	i+=1

b2 = 0
i = 0
while b > 0:
	b2 = b2 + ((b%10)*(2**i))
	b = b//10
	i+=1

print(str(bin(b1+b2))[2::])