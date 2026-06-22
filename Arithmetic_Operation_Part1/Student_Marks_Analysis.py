'''A student wants to calculate total marks, average, and percentage from 5 subjects.'''

M1,M2,M3,M4,M5 = map(int,input("Marks =").split())

total = M1 + M2 + M3 + M4 + M5
AVG =total/500
percentage = AVG

print("Total = ",total)
print("average = ",AVG)
print("Percentage = ",percentage)
