n = int(input("Enter a number: "))

l = len(str(n))
sq = n**n

if sq%(10**sq) == n :
	print(Automorphic Number)
else :
	print(Not a Automorphic Number)