'''A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.'''

amount = int(input("Total bill amount = "))
gst = int(input("GST = "))
service = int(input("Service charge = "))
friends = int(input("Number of friend = "))

gst = (amount*gst)/100
service = (amount*service)/100
bill = amount + gst + service
pay = bill/friends

print("Final Bill = ",bill)
print("Each Person Pays = ",pay)
