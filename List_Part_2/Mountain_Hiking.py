'''Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.'''

arr = []
N = int(input("Enter number of checkpoint: "))

for i in range(N):
	c = int(input("Enter checkpoint: "))
	arr.append(c)

peakindex = -1
for i in range(N):
	if i == 0 :
		if N==1 or arr[i] >= arr[i+1]:
			peakindex = i
			break
	elif i == N-1 :
		if arr[i] >= arr[i-1]:
			peakindex = i
			break
	else:
		if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
			peakindex = i
			break
if peakindex != -1 :
	print("Index of peakpoint:",peakindex)
	print("Peakpoint is",arr[peakindex])
else:
	print("Peak not found")