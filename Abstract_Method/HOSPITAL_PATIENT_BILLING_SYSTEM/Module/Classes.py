'''============================================================
                HOSPITAL PATIENT BILLING SYSTEM
===============================================================

Develop a MENU-DRIVEN Hospital Patient Billing System.

The hospital treats different categories of patients:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

Every patient must perform common operations such as:

calculate_bill()
calculate_discount()
calculate_final_amount()
generate_bill()

However, the calculation rules are different for each type
of patient.

Therefore, use ABSTRACTION to design the system.

------------------------------------------------------------
ABSTRACT CLASS:
------------------------------------------------------------

Create an abstract class:

Patient

It should contain appropriate abstract methods required for
billing.

Create the following child classes:

1. GeneralPatient
2. EmergencyPatient
3. InsurancePatient
4. CorporatePatient

------------------------------------------------------------
MAIN MENU:
------------------------------------------------------------

========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit

Enter your choice:

------------------------------------------------------------
OPTION 1: REGISTER PATIENT
------------------------------------------------------------

Input:

Patient ID
Patient Name
Patient Age

Then display:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

Enter patient type:

------------------------------------------------------------
GENERAL PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.500
Room Charge       : Rs.1000 per day
Medicine Charge   : Actual amount
Discount          : No discount

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
EMERGENCY PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.1000
Emergency Charge : Rs.500
Room Charge       : Rs.2000 per day
Medicine Charge   : Actual amount
Discount          : No discount

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
INSURANCE PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.800
Room Charge       : Rs.1500 per day
Medicine Charge   : Actual amount

Insurance covers 70% of the total hospital bill.

Patient pays remaining 30%.

Input:

Number of Days
Medicine Charge

------------------------------------------------------------
CORPORATE PATIENT:
------------------------------------------------------------

Consultation Fee : Rs.700
Room Charge       : Rs.1200 per day
Medicine Charge   : Actual amount

Corporate Discount = 20%

Input:

Number of Days
Medicine Charge'''

from abc import ABC , abstractmethod

class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        self.R_Charge =  self.Room_Charge*self.day
        self.calculate_discount()

    @abstractmethod
    def calculate_discount(self):
        self.t_h_b = self.Cons_Fee + self.R_Charge + self.M_Charge
        self.Discount_ammount = (self.t_h_b/100)*self.Discount
        self.calculate_final_amount()

    @abstractmethod
    def calculate_final_amount(self):
        self.Payable = self.t_h_b - self.Discount_ammount
        self.generate_bill()

    @abstractmethod
    def generate_bill(self):
        self.bill_Status = "GENERATED"

    @abstractmethod
    def display(self):
        print("""
========================================
            PATIENT BILL
========================================
""")
        self.calculate_bill()
        print("Patient ID       : ",self.id)
        print("Patient Name     : ",self.name)
        print("Patient Age      : ",self.age)
        print("Patient Type     : ",self.type)
        print()
        print("Consultation Fee : Rs",self.Cons_Fee)
        print("Room Charges     : Rs",self.R_Charge)
        print("Medicine Charges : Rs",self.M_Charge)
        print("""
        
        ----------------------------------------
        
        """)
        self.calculate_bill()

class GeneralPatient(Patient):
    Cons_Fee = 500
    Room_Charge = 1000
    Discount = 0
    type = "General"

    def calculate_bill(self):
        super().calculate_bill()

    def calculate_discount(self):
        super().calculate_discount()

    def calculate_final_amount(self):
        super().calculate_final_amount()

    def generate_bill(self):
        super().generate_bill()

    def display(self):
        super().display()
        print("Total Hospital Bill : Rs.",self.t_h_b)
        print("")
        print("Discount            :",self.Discount,"%")
        print("Discount Amount     : Rs.",self.Discount_ammount)
        print()
        print("Patient Payable     : Rs.",self.Payable)
        print()
        print("Bill Status         : ",self.bill_Status)
        print("""

========================================

""")

    
class EmergencyPatient(Patient):
    Cons_Fee = 1000
    Room_Charge = 2000
    Discount = 0
    type = "Emergency"

    def calculate_bill(self):
        super().calculate_bill()

    def calculate_discount(self):
        super().calculate_discount()
    
    def calculate_final_amount(self):
        super().calculate_final_amount()

    def generate_bill(self):
        super().generate_bill()

    def display(self):
        super().display()
        print("Total Hospital Bill : Rs.",self.t_h_b)
        print("")
        print("Discount            :",self.Discount,"%")
        print("Discount Amount     : Rs.",self.Discount_ammount)
        print()
        print("Patient Payable     : Rs.",self.Payable)
        print()
        print("Bill Status         : ",self.bill_Status)
        print("""

========================================

""")

class InsurancePatient(Patient):
    Cons_Fee = 800
    Room_Charge = 1500
    Discount = 70
    type = "Insurance"

    def calculate_bill(self):
        super().calculate_bill()

    def calculate_discount(self):
        super().calculate_discount()

    def calculate_final_amount(self):
        super().calculate_final_amount()

    def generate_bill(self):
        super().generate_bill()

    def display(self):
        super().display()
        print()
        print("Total Hospital Bill : Rs.",self.t_h_b)
        print("")
        print("Insurance Coverage  :",self.Discount,"%")
        print("Insurance Amount    : Rs.",self.Discount_ammount)
        print()
        print("Patient Payable     : Rs.",self.Payable)
        print()
        print("Bill Status         : ",self.bill_Status)
        print("""

========================================

""")
        
class CorporatePatient(Patient):
    Cons_Fee = 700
    Room_Charge = 1200
    Discount = 20
    type = "Corporate"

    def calculate_bill(self):
        super().calculate_bill()

    def calculate_discount(self):
        super().calculate_discount()

    def calculate_final_amount(self):
        super().calculate_final_amount()

    def generate_bill(self):
        super().generate_bill()

    def display(self):
        super().display()
        print("Total Hospital Bill : Rs.",self.t_h_b)
        print("")
        print("Discount            :",self.Discount,"%")
        print("Discount Amount     : Rs.",self.Discount_ammount)
        print()
        print("Patient Payable     : Rs.",self.Payable)
        print()
        print("Bill Status         : ",self.bill_Status)
        print("""

========================================

""")