# 1.Hello & Name Priner
print("Hello")
print("Khushi Sawanliya")
print("I am from Mandsaur")

# 2.Menu Display
print("=== Welcome to Coffee Shop ===")
print("1.Espresso\t$3")
print("2.Latte\t$4")
print("3.Cappuccino\t$5")
print("="*30)
 
# 3.Resume Format
print("===Resume===")
print("Name : Alice Johson")
print("Email : alice@example.com")
print("Skills :")
print("-Java","HTML & CSS","Problem Solving",sep="\n-")
print("2 yesrs at XYZLtd.")

# 4.Star Pattern
print("*"*5)
print("*"*5)
print("*"*5)

# 5.Special Characters
print("@ # $ % ^ & *")

# 6.Print User Details
name = input("enter your name : ")
age = int(input("enter your age : "))
city = input("enter your city : ")
print("Name : ",name)
print("Age : ",age)
print("City : ",city)

# 7.Full Name Display
fname = input("enter your first name : ")
lname = input("enter your last name : ")
print(fname," ",lname)

# 8.Simple Input Display
a = int(input("enter first number : "))
b = int(input("enter second number : "))
print(a,"\n",b)

# 9.Three Input Display
a,b,c = input("enter 3 values : ").split()
print(a,"\n",b,"\n",c)

# 10.Input and Echo
msg = input("Enter your massege :- ")
print("You entered:",msg)

# 11.Greeting Message
name = input("Enter your name : ")
print("hello ",name," \nWelcome to python")

# 12.Favorite Things
food = input("Enter your favorite food - ")
color = input("Enter your favorite color - ")
print("I like {} and my favorite color is {}".format(food,color))

# 13.College Details
clg = input("Enter College Name: ")
course = input("Enter Course Name: ")
year = int(input("Enter Passing Year: "))
print("College Name: ",clg)
print("Course Name: ",course)
print("Passing Year: ",year)

# 14.Email Display
email = input("enter your emil : ")
print("your email is: ",email)

# 15.Bio Data
name = input("Enter your name: ")
age = int(input("Enter your Age: "))
phone = input("Enter your Phone no.: ")
print("---Bio Data---")
print("Name: ",name)
print("Age: ",age)
print("Phone: ",phone)