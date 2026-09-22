import Module as m

while True:
    n = int(input("Enter choice: "))
    match n:
        case 1:
            lst = []
            for n in range(1,6):
                roll = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                marks = int(input("Enter Marks: "))
                obj = m.student(roll,name,marks)
                lst.append(obj)
                print()

            print("All Students:")
            for k in lst:
                print(k.roll_no,k.name,k.marks)

            print()
            print("Students having marks greater than 60:")
            for k in lst:
                if k.marks > 60:
                    print(k.roll_no,k.name,k.marks)

            print()
            hm = lst[0]
            print("Highest Marks:")
            for k in lst:
                if hm.marks < k.marks:
                    hm = k
            print(hm.roll_no,hm.name,hm.marks)

            print()
            print("Average Marks:")
            avg = 0
            for k in lst:
                avg += k.marks
            print(avg/5)
            print()

        case 2:
            lst = []
            for k in range(5):
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                salary = int(input("Enter Salary: "))
                dep = input("Enter Department: ")
                obj = m.employee(id,name,salary,dep)
                lst.append(obj)
                print()

            print("All Employees:")
            for k in lst:
                print(k.emp,k.name,k.salary,k.department)
            print()

            print("Employees with salary greater than 40000:")
            for k in lst:
                if k.salary > 40000:
                    print(k.emp,k.name,k.salary,k.department)
            print()

            print("Employees from IT Department:")
            for k in lst:
                if k.department == "IT":
                    print(k.emp,k.name,k.salary,k.department)
            print()

            print("Highest Salary Employee:")    
            hs = lst[0]
            for k in lst:
                if hs.salary < k.salary:
                    hs = k
            print(hs.emp,hs.name,hs.salary,hs.department)
            print()

            print("Total Salary:")
            total = 0
            for k in lst:
                total += k.salary
            print(total)
            print()

            print("Average Salary:")
            print(total/5)
            print()

        case 3:
            lst = []
            for i in range(5):
                id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = int(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                obj = m.Product(id,name,price,quantity)
                print()

            print("Average Salary:")
            for k in lst:
                print(k.id,k.name,k.price,k.quantity)
            print()

            print("Product Total Values:")
            for k in lst:
                print(k.name,"=",k.price*k.quantity)
            print()

            print("Low Stock Products:")
            for k in lst:
                if k.quantity < 10:
                    print(k.name)
            print()

            print("Highest Price Product:")
            hp = lst[0]
            for k in lst:
                if hp.price < k.price:
                    hp = k
            print(hp.name,"=",hp.price)
            print()

            print("Total Inventory Value:")
            value = 0
            for k in lst:
                value += k.price*k.quantity
            print(value)
            print()

            id = int(input("Enter Search Product Id: "))
            print()

            for k in lst:
                if k.id == id:
                    print("Product Fount:")
                    print(k.id,k.name,k.price,k.quantity)
                    break
                else:
                    print("Product Not Fount")

        case 4:
            lst = []
            for i in range(5):
                no = int(input("Enter Account Number: "))
                name = input("Enter Customer Name: ")
                balance = int(input("Enter Balance: "))
                obj = m.account(no,name,balance)
                lst.append(obj)
            print()

            no = int(input("Enter Account No: "))
            amount = int(input("Enter amount to deposite: "))
            print()

            for k in lst:
                if k.acc_no == no:
                    k.deposite(amount)
                    print("After Deposit:")
                    print(k.acc_no,k.name,k.balance)
                    break
            else:
                print("Account not found")
            print()

            print("Enter Account No: ")
            print("Enter amount to withdraw: ")
            print()

            for k in lst:
                if k.acc_no == no:
                    k.withdraw(amount)
                    print("After Withdrawal:")
                    print(k.acc_no,k.name,k.balance)
                    break
            else:
                print("Account not found")
            print()

            print("Accounts having balance greater than 50000:")
            for k in lst:
                if k.balace > 50000:
                    print(k.account,k.name,k.balance)
            print()

            print("Highest Balance Account:")
            h = lst[0]
            for k in lst:
                if k.balance > h.balance :
                    h = k
            print(k.account,k.name,k.balance)
            print()

        case 5:
            lst = []
            for i in range(5):
                id = int(input("Enter Book ID: "))
                name = input("Enter Book Name: ")
                author = input("Enter Author Name: ")
                price = int(input("Enter Price: "))
                obj = m.book(id,name,author,price)
                lst.append(obj)
            print()

            print("All Books:")
            for k in lst:
                print(k.id,k.name,k.author,k.price)
            print()

            print("Books by James:")
            for k in lst:
                if k.author == "James":
                    print(k.id,k.name,k.price)
            print()

            print("Books with price greater than 500:")
            for k in lst:
                if k.price > 500 :
                    print(k.id,k.name,k.price)
            print()

            print("Most Expensive Book:")
            exp = lst[0]
            for k in lst:
                if k.price > exp.price :
                    exp = k
            print(exp.id,exp.name,exp.price)
            print()

            print("Average Price:")
            avg = 0
            for k in lst:
                avg += k.price
            print(avg/5)
            print()

        case 6:
            lst = []
            for k in range(5):
                id = int(input("Enter Customer ID: "))
                name = input("Enter Customer Name: ")
                city = input("Enter City: ")
                amt = int(input("Enter Purchase Amount: "))
                obj = m.customer(id,name,city,amt)
                lst.append(obj)

            print("Customers from Indore:")
            for k in lst:
                if k.city == "Indore":
                    print(k.id,k.name,k.amount)
            print()

            print("Customers with purchase amount greater than 10000:")
            for k in lst:
                if k.amout > 10000:
                    print(k.id,k.name,k.amount)
            print()

            print("Highest Purchase Customer:")
            high = lst[0]
            for k in lst:
                if k.amount > high.amount:
                    high = k
            print(high.id,high.name,high.amount)
            print()

            print("Total Sales:")
            total = 0
            for k in lst:
                total += k.amount
            print(total)
            print()

            print("Average Purchase Amount:")
            print(total/5)
            print()

            id = int(input("Search Customer Id: "))
            for k in lst:
                if k.id == id:
                    print("Customer Found:")
                    print(k.id,k.name,k.city,k.amount)
                    print()
                    break
            else:
                print("Customer Not Found:")
                print()

        case 7:
            lst = []
            for i in range(5):
                id = int(input("Enter Movie Id: "))
                name = input("Enter Movie Name: ")
                genre = input("Enter genre: ")
                rate = float(input("Enter rating: "))
                price = int(input("Enter Ticket Price: "))
                obj = m.movie(id,name,genre,rate,price)
                lst.append(obj)
                print()

            print("Movies with rating greater than 8:")
            for k in lst:
                if k.rating > 8.0:
                    print(k.name,k.rating)
            print()

            print("Action Movies:")
            for k in lst:
                if k.genre == "Action":
                    print(k.name)
            print()

            print("Highest Rated Movie:")
            h = lst[0]
            for k in lst:
                if h.rating < k.rating:
                    h = k
            print(k.name,k.rating)

            print("Movies with ticket price greater than 300: ")
            for k in lst:
                if k.price > 300:
                    print(k.name,k.price)
            print()

            print("Average Movie Rating:")
            avg = 0
            for k in lst:
                avg += k.rating
            print(avg/5)
            print()

            id = input("Search Movie Id: ")
            for k in lst:
                if k.id == id:
                    print("Movie Found")
                    print(k.id,k.name,k.genre,k.rating,k.price)
                    print()
                    break
            else:
                print("Movie Not Found")
                break

        case 8:
            print("Thank you. Have a nive day!")
            break

        case __:
            print("Try again.")