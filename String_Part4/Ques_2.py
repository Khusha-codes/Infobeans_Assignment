n = input("Enter Number: ")
diff = ""
count = 0
l = 0
x = len(n)

for i in range(len(n)-1) :
	n1 = int(n[i])
	n2 = int(n[i+1])
	if n1 > n2 :
		d = n1 - n2
	else :
		d = n2 - n1
	if d > l :
		l = d
	count += d
	diff = diff + " " + str(d)

print("Step Differences:",diff)
print("Sum =",count)
print("Largest =",l)
if count % int(n) == 0 :
	print("Balanced Number") 
else :
	print("Unbalanced Number")


