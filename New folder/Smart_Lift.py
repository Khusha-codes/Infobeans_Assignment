'''Lift Mode Operation – Advanced Smart Elevator System


A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  

The system must automatically execute floor movement instructions using loops.'''

mode = int(input("Enter mode: "))

if mode == 1 :
	current = int(input("Enter current floor no.: "))
	destination = int(input("Enter Destination floor no.: "))
	if current > destination :
		print("Retry.")
	else :
		while current <= destination :
			print(current," ")
			current+=1

elif mode == 2 :
	current = int(input("Enter current floor no.: "))
	destination = int(input("Enter Destination floor no.: "))
	if current < destination :
		print("Retry.")
	else :
		while current >= destination :
			print(destination," ")
			destination-=1
elif mode == 3 :
	destination = int(input("Enter Destination floor no.: "))
	i = 0
	while i <= destination :
		print(i," ")
		i+=1

else :
	i = 1
	while i <= 4 :
		print("Emergency Alarm")
		i+=1

		