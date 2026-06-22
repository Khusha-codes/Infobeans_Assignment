'''A Python program that:
Accepts total amount.
Calculates 10% discount and final price.'''


amt = int(input("Amount = "))

dis = amt/10
final = amt - dis

print("Discount =",dis)
print("Final =",final)