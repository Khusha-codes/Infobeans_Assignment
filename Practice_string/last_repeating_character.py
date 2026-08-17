s = input("Enter string: ")
ch = ""
for i in s:
	if s.count[i] != 1 :
		ch = i
if ch :
	print(ch)
else :
	print("No repeating character")