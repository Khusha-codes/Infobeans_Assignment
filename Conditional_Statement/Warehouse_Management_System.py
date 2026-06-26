'''A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.'''

unit1 = int(input("Unit1 = "))
unit2 = int(input("Unit2 = "))
unit3 = int(input("Unit3 = "))
unit4 = int(input("Unit4 = "))
unit5 = int(input("Unit5 = "))
unit6 = int(input("Unit6 = "))

if unit1 > unit2 :
	if unit1 > unit3 :
		if unit1 > unit4 :
			if unit1 > unit5 :
				if unit1 > unit6 :
					print("Hightest Stock =",unit1)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
		else :
			if unit4 > unit5 :
				if unit4 > unit6 :
					print("Hightest Stock =",unit4)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
	else :
		if unit3 > unit4 :
			if unit3 > unit5 :
				if unit3 > unit6 :
					print("Hightest Stock =",unit3)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
		else :
			if unit4 > unit5 :
				if unit4 > unit6 :
					print("Hightest Stock =",unit4)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
else :
	if unit2 > unit3 :
		if unit2 > unit4 :
			if unit1 > unit5 :
				if unit2 > unit6 :
					print("Hightest Stock =",unit2)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
		else :
			if unit4 > unit5 :
				if unit4 > unit6 :
					print("Hightest Stock =",unit4)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
	else :
		if unit3 > unit4 :
			if unit3 > unit5 :
				if unit3 > unit6 :
					print("Hightest Stock =",unit3)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)
		else :
			if unit4 > unit5 :
				if unit4 > unit6 :
					print("Hightest Stock =",unit4)
				else :
					print("Hightest Stock =",unit6)
			else :
				if unit5 > unit6 :
					print("Hightest Stock =",unit5)
				else :
					print("Hightest Stock =",unit6)

