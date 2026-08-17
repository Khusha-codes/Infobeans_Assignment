'''Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.'''

com = input("Enter command: ").split()
temp = com[0]
for ch in com:
	if ch not in temp:
		temp = temp + " " + ch
print(temp)