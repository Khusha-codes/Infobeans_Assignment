'''Employee Bonus Calculation (Using filter() and map() with Lambda Expressions)

A software company wants to reward its high-performing employees with a 10% bonus. However, only employees earning ₹50,000 or more are eligible for
 the bonus.

As a software developer, your task is to:

Filter the salaries of eligible employees.
Calculate the updated salary after adding a 10% bonus.
Display the final salaries of the eligible employees.

Note: Use filter() to identify eligible employees and map() to calculate the updated salaries. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of employees.
The second line contains N space-separated salary values.
Output Format

Display the updated salaries of all eligible employees after adding a 10% bonus.'''

n = int(input("Enter number of employees: "))
print("Enter the salaries: ")
sal = map(int,input().split())
f = list(filter(lambda n:n >= 50000 ,sal))
print(list(map(lambda n:(n*11)/10,f)))