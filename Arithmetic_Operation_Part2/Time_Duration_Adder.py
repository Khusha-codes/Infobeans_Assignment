'''A Python program that:
Accepts hours, minutes, seconds.
Converts into total seconds.'''

h = int(input("Hours = "))
m = int(input("Minutes = "))
s = int(input("Seconds = "))

sec = s + m*60 + h*3600

print("Total Seconds =",sec)