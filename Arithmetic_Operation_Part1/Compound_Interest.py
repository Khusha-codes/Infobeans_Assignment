'''A person invests money in a bank that provides compound interest annually.'''

principal = int(input("Principal = "))
rate = int(input("Rate = "))
time = int(input("Time = "))

amount = principal*(1 + (rate/100))**time

print("Amount after interest = ",amount)
