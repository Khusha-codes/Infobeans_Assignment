s = input("Enter string: ")

w = ""

for i in range(len(s)):
	if s[i] == " ":
		if w == w[::-1]:
			print(w)
			break
		w = ""
		continue
	w += s[i]
else:
	print("No palindrome")