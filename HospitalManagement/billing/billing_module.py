bill = {}

def generate_bill(id,fees,cost,test):
	bill["Patient ID"] = id
	bill["Consultation Charges"] = fees
	bill["Medicine Cost"] = cost
	bill["Test Charges"] = test
	bill["Total"] = fees + cost + test
	for k,v in bill.items():
		print(k,":",v,"\n")
	
