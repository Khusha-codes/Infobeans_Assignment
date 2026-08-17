n = int(input("Enter size: "))
l = []
for i in range(n):
	x = int(input("Enter element: "))
	l.append(x)
k = int(input("Enter number of times you want to rotate: "))
while k > 0 :
	last = l[-1]
	i = len(l) -1
	while i > 0 :
		l[i] = l[i-1]
		i-=1
	l[0] = last
	k-=1
print(l) 