'''An employee wants to calculate salary per day and per hour'''

salary = int(input("Monthly salary = "))
days = int(input("Working days = "))
hours = int(input("Working hours per day = "))

per_day = salary/days
per_hour = per_day/hours

print("Salary per day = ",per_day)
print("Salary per day = ",per_hour)
