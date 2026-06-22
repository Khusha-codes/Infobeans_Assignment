'''Convert total seconds into hours, minutes, and seconds.'''

sec = int(input("Time second = "))
hours = sec//3600
minutes = (sec%3600)//60
second = sec%60
print("Hours =",2,"\nMinutes =",minutes,"\nSeconds =",second)