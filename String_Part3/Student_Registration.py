'''Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”'''

code = input("Enter registration code: ").lower()
alpha = ""
num = ""

for ch in code :
	if ch.isalpha() and ch not in alpha :
		alpha += ch
	elif ch.isdigit() :
		num += ch

word = sorted(alpha)
final = "".join(word)
num = sorted(num)

i = len(num)
while i > 0 :
	final += num[i-1]
	i-=1

print("Result:",final)