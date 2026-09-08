S = input("Enter String: ")
pre = input("Prefix: ")
suf = input("Suffix: ")

i = 0
while i < len(pre):
	if pre[i] != S[i]:
		print("Start: False", end =" ")
		break
	i += 1
else:
	print("Start: True", end =" ")

j = 1
while j <= len(suf):
	if suf[-j] != S[-j]:
		print("End: False")
		break
	j += 1
else:
	print("End: True")