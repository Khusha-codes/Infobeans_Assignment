n1 = int(input("Enter first number: "))
n2 = int(input("Enter last number: "))
sum = 0

for i in range(n1,n2+1) :
	if i%4 == 0 :
		print(i,"-> Event Scheduled")
		sum+=1
	else :
		print(i,"-> No Event")

print()
print("Total Leap Years =",sum)
print("Total Events Schedules =",sum)