'''A Python program that:
Accepts principal, rate, and time.
Calculates compound interest.'''

p = int(input("Principal = "))
r = int(input("Rate = "))
t = int(input("Time = "))

amt = p*((1 + (r/100))**t)
ci = amt - p

print("Amount = ",amt)
print("Compound Interest = ",ci)