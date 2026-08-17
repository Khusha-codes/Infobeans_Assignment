'''A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.'''

from collections import namedtuple
player = namedtuple("play",["player_id","player_name","run"])

n = int(input("Enter number of players: "))

lst = []
for i in range(n):
	print("Enter details")
	id = input("Enter player id: ")
	name = input("Enter player name: ")
	score = int(input("Enter player score: "))
	s = product(id,name,score)
	lst.append(s)
print()

total = 0
low = lst[0.rum]
max = lst[0.run]
print("All Players:")
for i in lst:
	total += i.run
	if max < i.rum :
		max == i.run
	if low > i.run :
		low == i.run
	print(*i)
print()

print("Highest Scorer:")
for i in lst:
	if i.run == max:
		print(*i)
print()

print("Lowest Scorer:")
for i in lst:
	if i.run == low:
		print(*i)
print()

print("Total Runs:")
print(total)
print()

print("Average Runs:")
print(total/n)
print()

print("Players Scoring More Than 50 Runs:")
for i in lst
	if i.run > 50:
		print(*i)


