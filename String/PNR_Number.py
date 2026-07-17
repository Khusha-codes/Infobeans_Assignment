'''Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits'''

pnr = input("Enter PNR: ")

if pnr[0:3] == "PNR" and len(pnr) == 12 and pnr[3::].isdigit() :
	print("Valid PNR Number")
else :
	print("Invalid Number")