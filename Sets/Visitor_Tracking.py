'''A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit'''

while true :
	print('''
Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit
''')

	n = int(input("Enter your Choice: "))
	print()
	vis = set()

	match n:
		case 1:
			no = int(input("Enter number of visitor: "))
			print()
			lst = []
			for i in no :
				lst.append(int(input("Enter visitor ID: ")))
			vis.update(lst)
			print()
		case 2:
			id = int(input("Enter visitor ID: "))
			if id in vis:
				vis.remove(id)
			print()
		case 3:
			id = int(input("Enter visitor ID: "))
			if id in vis:
				print("Yesss")
			else:
				print("Nooo")
			print()
		case 4:
			pass	
			# print()
		case 5:
			print("Visitors count:")
			print(len(vis))
			print()
		case 6:
			vis.clear()
			print()
		case 7:
			break
		case __:
			print("Try Again")
			print()