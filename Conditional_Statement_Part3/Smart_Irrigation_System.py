'''A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.'''

soil = int(input("Soil Moisture ="))
temp = int(input("Temperature = "))
crop = input("Crop = ")

if soil <= 30 :
	if temp >= 35 :
		if crop.lower == "wheat" :
			print("Irrigation = High Water Supply.")
		else :
			print("Irrigation = Moderate Supply.")
	else :
		print("Irrigation = Moderate Supply.")
else :
	if soil >= 60 :
		print("Irrigation = Delay Irrigation.")
	else :
		print("Irrigation = Light Irrigation.")
else :
	print("Irrigation = No Irrigation.")