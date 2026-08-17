'''Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000'''

n = int(input("Enter number of employee: "))
salary = []
sum = 0
for i in range(n):
	s = int(input("Enter salary: ")) 
	salary.append(s)
	sum += s
avg = sum/n
ab = []
for i in salary :
	if i > avg :
		ab.append(i)
print("Average salary is",avg)
print("Salary above average",ab)
for i in salary :
	if i < 15000 :
		salary.remove(i)
	else :
		print(i)
print("Remaining salary are",salary)

