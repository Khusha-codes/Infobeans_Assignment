'''A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert'''

temp = int(input("Enter temperature: "))
humi = int(input("Enter humidity: "))

if temp >=30 :
	print("Hot day")

if humi >= 70 :
	print("High  humidity alert")