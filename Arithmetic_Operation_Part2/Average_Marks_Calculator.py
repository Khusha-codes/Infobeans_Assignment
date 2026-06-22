'''A Python program that:
Accepts marks of 3 subjects.
Calculates average.'''

m1,m2,m3 = map(int,input("Marks =").split())

sum = m1 + m2 + m3
avg = sum/3

print("Average =",avg)
