'''A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

====================================================== Choice 4
======================================================

Program Closed Successfully'''

while True :

	print("====================================================== MENU")
	print("======================================================")
	print()
	print("===== Smart Text Processing System =====")
	print()
	print("1.  Reverse Complete String")
	print("2.  Reverse Every Word")
	print("3.  Reverse Word Order")
	print("4.  Exit")
	print()

	choice = int(input("Enter your choice: "))

	match choice :
		case 1 :
			msg = input("Input: ")
			temp = ""

			for ch in msg :
				if ch.alpha() :
					pass
				temp += ch
			print("======================================================")
			print("======================================================")
		case 2 :
			msg = input("Enter: ")
			word = ""
			temp = ""
			for ch in msg :
				if ch == " ":
					i = 1
					while i <= len(word) :
						temp += word[-i]
						i+=1
					temp += " "
					word = ""
				else :
					word += ch 
				i = 1
				while i <= len(word) :
					temp += word[-i]
					i+=1
			print(temp)
			print("======================================================")
			print("======================================================")
		case 3 :
			msg = input("Enter: ")
			word = ""
			temp = ""
			for ch in msg :
				if ch == " ":
					temp += temp + " " + word
				else :
					word += ch 
			temp += temp + " " + word
			print(temp)
			print("======================================================")
			print("======================================================")
		case 4 :
			print("======================================================")
			print()
			print("Program Closed Successfully")
			print("======================================================")
			break 




	