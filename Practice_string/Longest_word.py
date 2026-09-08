s = input("Enter string: ")
larg = ""

w = ""

for i in range(len(s)):
	if s[i] == " ":
		if len(w) > len(larg):
			larg = w
		w = ""
		continue
	w += s[i]

if len(w) > len(larg):
	larg = w

print(larg)