'''A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000'''

distance = int(input("Enter distance: "))
Class = input("Enter class: ")

if distance <= 100 :
	if Class.lower() == "ac" :
		print("Total Fare = ₹200")
	else :
		print("Total Fare = ₹100")
elif distance <= 500 :
	if Class.lower() == "ac" :
		print("Total Fare = ₹600")
	else :
		print("Total Fare = ₹300")
else :
	if Class.lower() == "ac" :
		print("Total Fare = ₹1000")
	else :
		print("Total Fare = ₹500")