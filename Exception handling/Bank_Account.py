''' BANK ACCOUNT MANAGEMENT SYSTEM

Scenario:
A bank wants to develop a simple Python-based application to manage customer
bank accounts.

The application must handle invalid transactions using custom exceptions.

Create a class named BankAccount with the following attributes:

1. account_number
2. account_holder
3. balance

Create the following custom exceptions:

1. InsufficientBalanceException
2. NegativeDepositException
3. InvalidWithdrawalException
4. InvalidAmountException

## Requirements:

Create the following methods:

1. deposit(amount)
2. withdraw(amount)
3. check_balance()
4. display_account_details()

## deposit(amount):

1. If the deposit amount is negative, raise:

   NegativeDepositException: Deposit amount cannot be negative

2. If the deposit amount is zero, raise:

   InvalidAmountException: Deposit amount must be greater than zero

3. Otherwise, add the amount to the account balance.

4. Display the updated balance.

## withdraw(amount):

1. If the withdrawal amount is negative, raise:

   InvalidWithdrawalException: Withdrawal amount cannot be negative

2. If the withdrawal amount is zero, raise:

   InvalidAmountException: Withdrawal amount must be greater than zero

3. If the withdrawal amount is greater than the available balance, raise:

   InsufficientBalanceException: Insufficient balance

4. Otherwise, deduct the amount from the balance.

5. Display the updated balance.

## MENU:

The program should be menu-driven.

Display the following menu repeatedly:

================================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit

Enter your choice:

## Functional Requirements:

Option 1:
Ask the user for the deposit amount and perform the deposit operation.

Option 2:
Ask the user for the withdrawal amount and perform the withdrawal operation.

Option 3:
Display the current account balance.

Option 4:
Display:

Account Number:
Account Holder:
Available Balance:

Option 5:
Display:

Thank you for using Bank Account System

For invalid menu choices, display:

Invalid choice

## Exception Handling:

Every transaction must be handled using try-except.

The program should NOT terminate when an exception occurs.

After displaying the exception message, the menu should be displayed again.'''

class InvalidAmountException(Exception):
    pass

class InvalidWithdrawalException(Exception):
    pass

class InvalidAmountException(Exception):
    pass

class InsufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,acc_no,acc_holder,balance):
        self.acc_no = acc_no
        self.holder = acc_holder
        self.balance = balance

    def deposit(self,amount):
        if amount<0:
            raise InvalidAmountException("Deposit amount cannot be negative")
        elif amount == 0:
            raise InvalidAmountException("Deposit amount must be greater than zero")
        else:
            self.balance += amount
        self.check_balance()

    def withdrow(self,amount):
        if amount<0:
            raise InvalidWithdrawalException("Withdrawal amount cannot be negative")
        elif amount == 0:
            raise InvalidAmountException("Withdrawal amount must be greater than zero")
        elif amount > self.balance:
            raise InsufficientBalanceException("Insufficient balance")
        else:
            self.balance -= amount
            self.check_balance()

    def check_balance(self):
        print("Your current balance: ",self.balance)

    def display_account_details(self):
        print("Account number: ",self.acc_no)
        print("Account holder: ",self.holder)
        print("Balamce       : ",self.balance)

a_no = int(input("Enter account number: "))
holder = input("Account holder: ")
balance = int(input("Enter account balance"))
p = BankAccount(a_no,holder,balance)

while True:
    try:
        print("""
===================
BANK ACCOUNT SYSTEM
===================

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit
""")
        n = int(input("Enter Your choice: "))
        print()
        match n:
            case 1:
                amount = int(input("Enter deposit amount: "))
                p.deposit(amount)
            case 2:
                amo = int(input("Enter withdrow amount: "))
                p.withdrow(amo)
            case 3:
                p.check_balance()
            case 4:
                p.display_account_details()
            case 5:
                print("Thank you for using Bank Account System")
                break
            case __:
                print("PLease enter a valid choice")
    except Exception as e:
        print(e)