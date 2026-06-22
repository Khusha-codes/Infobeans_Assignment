'''A Python program that:
Accepts distance1, time1, distance2, time2.
Calculates average speed.'''

dist1 = int(input("Distance1 = "))
time1 = int(input("Time1 = "))
dist2 = int(input("Distance2 = "))
time2 = int(input("Time2 = "))

speed1 = dist1/time1
speed2 = dist2/time2
avg = (speed1 + speed2)/2
print("Average Speed = ",avg,"km/h")
