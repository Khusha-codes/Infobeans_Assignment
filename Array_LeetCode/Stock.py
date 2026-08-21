'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

n = int(input("Enter number of element: "))
lst = []

for i in range(n):
	lst.append(int(input("Enter element: ")))

l = 0
for i in range(n):
	if lst[l] > lst[i] :
		l = i

m = len(lst) - 1
for i in range(l,n):
	if lst[m] < lst[i] :
		m = i

print(lst[m] - lst[l])