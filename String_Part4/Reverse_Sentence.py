'''Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.'''

msg = input("Enter message: ").split()
i = len(msg) - 1
temp = ""

while i >= 0 :
	word = msg[i]
	temp = temp + word[::-1] + " "
	i -= 1

print("Output",temp)