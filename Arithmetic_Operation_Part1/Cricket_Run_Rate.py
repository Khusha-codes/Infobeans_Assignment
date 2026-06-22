'''In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.'''

runs = int(input("Total runs ="))
over1,over2 = map(float,input("Run Rate =").split("."))

balls = (over1*6)+over2
rate = float(runs/(balls/6))

print("Total Balls = ",balls)
print("Run Rate = ",rate)