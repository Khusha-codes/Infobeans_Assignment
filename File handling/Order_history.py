'''An e-commerce company maintains order information in orders.txt.

Each order contains:

OrderID,CustomerName,Product,Quantity,Price
Task

Write a program to:

Accept order details.
Store them in the file.
Read the file.
Calculate total amount for each order.
Display the order having the highest total amount.

Formula:

Total Amount = Quantity × Price'''
try:
#     n = int(input("Enter number of orders: "))
#     with open("order_details.txt","a") as f:
#         for i in range(n):
#             id = input("Enter Order ID: ")
#             name = input("Enter Customer Name: ")
#             product = input("Enter Product Name: ")
#             quantity = int(input("Enter Quantity: "))
#             price = int(input("Enter Price: "))
#             f.write(f"{id} {name} {product} {quantity} {price}\n")
    with open("order_details.txt","r") as f:
        high = 0
        print("""Order Details
--------------------------------""")
        for line in f:
            l = line.strip().split()
            total = int(l[3])*int(l[4])
            print(f"{l[0]} {l[1]} {l[2]} Quantity: {l[3]} Total: {total}")
            if total > high:
                high = total
                a = l
        print()
        print("Highest Order:")
        print("Order ID: ",a[0])
        print("Customer: ",a[1])
        print("Total Amount: ",high)
        print("================")
finally:
    print("Done")


    