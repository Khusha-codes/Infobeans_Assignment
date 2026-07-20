'''Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com'''

web = input("Enter website: ")

if web[0:3] == "www" and web[len(web)-4:len(web)] == ".com" :
	print("Valid Website")
else :
	print("Invalid Website")