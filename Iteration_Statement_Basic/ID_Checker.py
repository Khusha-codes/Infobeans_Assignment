'''A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.'''

n = int(input("Enter number : "))
odd = 0

while n>0 :
	if (n%10)%2 != 0 :
		odd += 1
	n = n//10 
print("Number of odd digit are : ",odd)