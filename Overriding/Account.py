'''Create a parent class BankAccount with:

account_no
holder_name
balance

Create two child classes:

SavingsAccount
CurrentAccount
Requirements
Take account details from the user.
Use super() to initialize the common attributes.
Create a method calculate_interest() in the parent class.
Override this method in both child classes.
Savings Account gets 5% interest.
Current Account gets 2% interest.
Display the account details and calculated interest.'''

class BankAccount:
    def __init__(self,no,name,balance):
        self.no = no
        self.name = name
        self.balance = balance

    def calculate_interest(self):
        self.interest = "100%"
        self.inter = self.balance*100

class SavingAccount(BankAccount):
    def __init__(self, no, name, balance):
        super().__init__(no, name, balance)

    def calculate_interest(self):
        self.interest = "5%"
        self.inter = self.balance/20

class CurrentAccount(BankAccount):
    def __init__(self, no, name, balance):
        super().__init__(no, name, balance)

    def calculate_interest(self):
            self.interest = "2%"
            self.inter = self.balance/50

no = int(input("Enter Account Number: "))
name = input("Enter Holder Name: ")
balance = int(input("Enter Balance: "))
type = input("Enter Account Type: ").lower()

if type == "current":
    obj = CurrentAccount(no,name,balance)
else:
    obj = SavingAccount(no,name,balance)

obj.calculate_interest()
print("----- Account Details -----")
print("Account Number : ",obj.no)
print("Holder Name    : ",obj.name)
print("Balance        : ",obj.balance)
print("Account Type   : ",type)
print("Interest Rate  : ",obj.interest)
print("Interest       : ",obj.inter)
print("Amount After Interest : ",obj.balance+obj.inter)
    