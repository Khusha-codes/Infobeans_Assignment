s = input("Enter string: ")
temp = ""
l = 0
r = len(s) - 1
while r < len(s) - 1 and l >= 0 :
	if s[l].isalnum() and s[r].isalnum() :
		print(s[l] ,"and", s[r])
		temp += s[r]
		l+=1
		r-=1
	elif s[l] in ["!","@","#","$","%","^","&","*","(",")","_",] and s[r].isalnum() :
		temp += s[l]
		l+=1
	elif s[l].isalnum() and s[r] in ["!","@","#","$","%","^","&","*","(",")","_",] :
		r-=1
	else :
		l+=1
		r-=1
	print(temp)
print(temp)