n = int(input("Enter a number"))
rev = 0
sq = n**2

while n>0 :
	rev  = rev*10 + n%10
	n = n//10

temp = 0
rev = rev**2
while rev > 0 :
	temp = temp*10 + rev%10
	rev = rev//10
if rev == sq :
	print("Adam Number")
else :
	print("Not a Adam Number")