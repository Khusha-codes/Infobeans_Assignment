s = input("Enter string: ")
s = s + " "
result = ""

w = ""

for i in range(len(s)):
	if s[i] == " ":
		result = w + " " + result
		w = ""
		continue
	w += s[i]

print(result)