n = int(input("Enter number: "))

sum = 0
product = 1

while n > 0 :
	product = product*(n%10)
	sum += n%10
	n = n//10

if sum == product :
	print("Spy Number")
else :
	print("Not a spy number.")
