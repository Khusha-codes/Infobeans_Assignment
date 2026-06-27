'''An airline calculates ticket price based on class, distance, and booking time.

If class is business, then check distance. If distance is greater than 1000, price is 8000; otherwise 5000.

If class is economy, then check distance. If distance is greater than 1000, then check booking time. If booking is early, price is 4000; otherwise 5000. If distance is less than or equal to 1000, price is 2500.'''

class = input("Class = ")
distance = int(input("Distance = "))
booking = input("Booking = ")

if class.lower() == "business" :
	if distance > 1000 :
		print("Ticket Price = 8000")
	else :
		print("Ticket Price = 5000")
elif class.lower() == "economy" :
	if distance > 1000 :
		if booking.lower() == "early" :
			print("Ticket Price = 4000")
		else :
			print("Ticket Price = 5000")
	else :
		print("Ticket Price = 2500")