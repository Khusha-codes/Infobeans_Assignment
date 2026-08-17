'''A bike needs service every 3000 km.


Write a program to:


- Read travelled kilometers

- Print every service checkpoint till entered km'''

n = int(input("Enter kilometer: "))
i = 1

while n >= 3000:
	print(i*3000,end=" ")
	n = n - 3000
	i+=1