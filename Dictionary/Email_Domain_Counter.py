'''emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.'''

emails = ["[ajay@gmail.com](mailto:ajay@gmail.com)","[ravi@yahoo.com](mailto:ravi@yahoo.com)","[neha@gmail.com](mailto:neha@gmail.com)","[aman@outlook.com](mailto:aman@outlook.com)","[abc@gmail.com](mailto:abc@gmail.com)"]

d = {}

for x in emails:
	s = x.rfind("@") + 1
	d[x[s:-2]] = d.get(x[s:-2],0) + 1

for k,v in d.items():
	print(k," : ",v)

	