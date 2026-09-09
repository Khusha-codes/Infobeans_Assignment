'''A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.'''

from functools import reduce

players = [("Virat", 78),("Rohit", 102),("Gill", 89),("KL Rahul", 65),("Iyer", 91)]

name = reduce(lambda a,b:a if a[1]>b[1] else b, players)

print("Highest Run Scorer:",name[0])