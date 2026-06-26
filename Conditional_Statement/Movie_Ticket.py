'''A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input.
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening,
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.'''

age = int(input("Age : "))
time = input("Show Time(morning/evening) : ")
day = input("Day(weekday/weekend) : ")

if age <= 18 :
	if time.lower() == "morning" :
		print("Ticket Price is 100.")
	else :
		print("Ticket Price is 150.")
else :
	if time.lower() == "evening" :
		if day.lower() == "weekend" :
			print("Ticket Price is 300.")
		else :
			print("Ticket Price is 250.")
	else :
		print("Ticket Price is 200.")