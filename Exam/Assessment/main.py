import string_operations as so 
import list_operations as lo

while True:
    print('''========== MENU ==========

1. Print All Substrings
2. Minimum Size Subarray Sum
3. Exit
''')
    n = int(input("Enter your choice:"))

    match n:
        case 1:
            str = input("Enter a string: ")
            so.substring(str)
            print()
        case 2:
            n = int(input("Enter number of elements:"))
            lst = []
            print("Enter elements: ")
            for i in range(n):
                J = int(input())
                lst.append(J)
            print()
            t = int(input("Enter target: "))
            lo.subarray(lst,t)
            print()
        case 3:
            print("Thank You")
            break
        case __:
            print("Invalid choice. Please enter a valid choice.")
    