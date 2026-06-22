'''A Python program that:
Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.'''

amt = int(input("Amount = "))

hun = amt//100
fif = (amt%100)//50
ten = (amt%50)//10

print("Rs100 x ",hun)
print("Rs50 x ",fif)
print("Rs10 x ",ten)