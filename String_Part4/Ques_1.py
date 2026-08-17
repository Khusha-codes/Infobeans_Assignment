n = int(input("Enter number: "))
rev = 0
temp = n
while temp > 0 :
	rev = rev*10 + temp%10
	temp = temp//10

if rev > n :
	diff = rev - n
elif n > rev :
	diff = n - rev
else :
	diff = 0
count = len(str(diff))

print("Reverse =",rev,end ="")
print("Difference =",diff,end ="")
print("Digits =",count,end ="")

if diff == 0 :
	print("Perfect Match")
elif diff%9 == 0 :
	print("Verified")
else :
	print("Rejected")