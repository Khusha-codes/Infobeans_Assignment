msg = input("Enter message: ").split()

rev = msg[::-1]
result = ""

for w in rev:
	word = w[::-1]
	result = result + word + " "
	
print("Reverse is:",result)


		