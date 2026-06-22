'''You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.'''

price = int(input("Mobile price = "))
downpay = int(input("Down payment = "))
interest = int(input("Interest rate = "))
month = int(input("Months = "))

remain = price - downpay
total = (remain*interest)/100 + remain
emi = total/month 

print("Remaining Amount = ",remain)
print("Total with Interest = ",total)
print("Mothly EMI = ",emi)