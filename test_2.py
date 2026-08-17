m = input("Enter a number: ")
n = int(m)
print(m)
print(n)
if len(str(n)) != len(m):
	print("Not a Duck Number.")
else:
	while n>0 :
		if n%10 == 0 :
			print("Duck Number.")
			break
		n = n//10
	else :
		print("Not a Duck Number.")