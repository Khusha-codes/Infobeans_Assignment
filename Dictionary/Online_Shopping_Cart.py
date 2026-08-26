'''A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.'''

d = eval(input("Enter dictionary: "))
quan = 0
for k,v in d.items() :
	quan += v

print("Quantity =",quan)