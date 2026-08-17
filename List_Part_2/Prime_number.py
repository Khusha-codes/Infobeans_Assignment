'''A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)'''

l = map(int,input("Enter List: ").split())
p = []
sum = 0
for i in l:
	if i > 0 :
		j = 2
		while j <= i/2:
			if i%j == 0 :
				break
			j+=1
		else :
			p.append(i)
			sum += i
if p :
	c = len(p)
	max = sorted(p)[-1]
else :
	c = 0
	max = -1
print("Prime IDs =",p)
print("Sum =",sum)
print("Max =",max)
print("Count =",c)