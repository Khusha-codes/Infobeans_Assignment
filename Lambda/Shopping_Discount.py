'''Online Shopping Discount (Using filter() and map() with Lambda Expressions)

An online shopping website is running a Festive Sale. Customers who purchase products worth ₹2,000 or more are eligible for a 20% discount.

As a software developer, your task is to:

Filter the prices of products that are ₹2,000 or more.
Calculate the discounted price by applying a 20% discount.
Display the final discounted prices.

Note: Use filter() to identify eligible products and map() to calculate the discounted prices. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of products.
The second line contains N space-separated product prices.
Output Format

Display the discounted prices of all eligible products.
'''

n = int(input("Enter number of product: "))
pro = map(int,input("Enter the product prices: ").split())
f = filter(lambda x: x >= 2000,pro)
print(list(map(lambda x:((x*8)/10),f)))