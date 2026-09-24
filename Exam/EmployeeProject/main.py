import models as m

emp = []
for i in range(5):
    id = int(input("Enter Enployee ID: "))
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    obj = m.Employee(id,name,dept,salary)
    emp.append(obj)
    
pjt = []
for i in range(5):
    id = int(input("Enter Project id: "))
    name = input("Enter Project name: ")
    emp_id = int(input("Enter Enployee id: "))
    cost = int(input("Enter Project Cost: "))

    obj = m.Project(id,name,emp_id,cost)
    pjt.append(obj)

while True:
    print("""========== MENU ==========

1. Display All Employees(.5 marks)
2. Search Employee by ID(.5 marks)
3. Display Employees by Department(.5 marks)
4. Find Highest Paid Employee(.5 marks)
5. Display Employee Projects(.5 marks)
6. Find Highest Cost Project(.5 marks)
7. Exit
""")
    n = int(input("Enter your choice: "))
    match n:
        case 1:
            for i in emp:
                print(i.id,i.name,i.department,i.salary)
        case 2:
            id = int(input("Enter Employee ID: "))

            for i in emp:
                if i.id == id:
                    print(i.id,i.name,i.department,i.salary)
                    break
            else:
                print("Employee Not Found")
        case 3:
            d = input("Enter Department name: ")
            for i in emp:
                if i.department == d:
                    print(i.id,i.name,i.department,i.salary)
        case 4:
            h = emp[0]
            for i in emp:
                if i.salary > h.salary:
                    h = i
            print(h.id,h.name,h.department,h.salary)
        case 5:
            id = int(input("Enter Employee ID: "))
            for i in pjt:
                if i.emp_id == id:
                    print(i.id,i.name,i.emp_id,i.cost)
        case 6:
            h = pjt[0]
            for i in pjt:
                if i.cost > h.cst:
                    h = i
            print(h.id,h.name,h.emp_id,h.cost)
        case 7:
            print("Thank you")
            break
        case __:
            print("Invalid choice. Please enter a valid choice.")