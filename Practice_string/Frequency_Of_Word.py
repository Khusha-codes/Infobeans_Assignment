S = input("Enter string: ")
w = ""

for i in range(len(S)):
	if S[i] == " ":
		print(w, S.count(w),end = " ")
		w = ""
		continue
	w += S[i]
