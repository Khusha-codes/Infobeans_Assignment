'''A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.'''

speed = int(input("Speed = "))
timeh = int(input("Time(hours) = "))
timem = int(input("Time(minutes) = "))

time = timeh + timem/60
dis = speed*time

print("Total Time = ",time," hours")
print("Distance = ",dis,"km")
