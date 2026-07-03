'''A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled'''

a = int(input("Enter Starting Year: "))
b = int(input("Enter Ending Year: "))

leap_year = 0
for k in range(a,b+1) :
	if k%4 == 0 :
		leap_year +=1
		print(k,"-> Event Scheduled")
	else :
		print(k,"-> No Event")
print("Total Leap Years =",leap_year)
print("Total Events Scheduled =",leap_year)