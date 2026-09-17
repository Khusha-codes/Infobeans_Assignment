'''A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST'''

class Guest:
    def __init__(self,id,name,day,charge):
        self.id = id
        self.name = name
        self.day = day
        self.charge = charge

    def Calculations(self):
        self.bill = self.day*self.charge
        self.gst = (self.bill*12)/100
        self.final = self.bill + self.gst

    def Display(self):
        print("Guest ID              : ",self.id)
        print("Guest Name            : ",self.name)
        print("Number of Days        : ",self.day)
        print("Room Charge Per Day   : ",self.charge)
        print("Room Bill             : ",self.bill)
        print("GST (12%)             : ",self.gst)
        print("Final Bill            : ",self.final)

id = input("Enter Guest ID : ")
name = input("Enter Guest Name : ")
day = int(input("Enter Number of Days : "))
charge = int(input("Enter Room Charge Per Day : "))

gst = Guest(id,name,day,charge)
gst.Calculations()
gst.Display()
