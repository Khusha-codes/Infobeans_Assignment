'''ONLINE SHOPPING SYSTEM

Scenario:

An e-commerce company wants to develop an Online Shopping System.
 The application should be menu-driven and should demonstrate different types of arguments used in Python functions.

MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit'''

lst = {}
pro = {}
gen = []

def reg(name,email,mobile,/):
	l = []
	l.append(name)
	l.append(email)
	l.append(mobile)
	lst[name] = l
	return "Customer Registered Successfully"

def pro(*,name,price,category):
	p = []
	p.append(name)
	p.append(price)
	p.append(category)
	pro[name] = p
	return "Product Details Displayed Successfully"

def gen(name="Laptop",price=55000):
	p = []
	p.append(name)
	p.append(price)
	gen.append(p)
	return "Invoice Generated Successfully"

def mul_pro(*pro):
	total = 0
	for i in pro:
		total += i
	return total

def dis(**dic):
	for k,v in dic.items():
		print(k,"and",v)

while True:
	print('''MENU

1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit'''
)
	print()
	n = int(input("Enter Choice: "))
	print()
	match n:
		case 1:
			name = input("Enter Name: ")
			email = input("Enter Email: ")
			mobile = int(input("Enter Mobile Number: "))
			print(reg(name,email,mobile))
		case 2:
			name = input("Enter Product Name: ")
			price = int(input("Enter Price: "))
			cate = input("Enter Category: ")
			print(pro(name=name,price=price,category=cate))
		case 3:
			pro_name = input("Enter Product Name: ")
			price = int(input("Eneter Prcie"))
			print(gen(pro_name,price))
		case 4:
			m = int(input("Enter Number of Products: "))
			l = []
			for x in range(m):
				l.append(int(input("Enter Price: ")))
			print(mul_pro(*(l)))
		case 5:
			print(dis(**lst))
		case 6:
			print("Thank You. Program Terminated.")
			break
		case __:
			print("Invalid Choice Try Again")