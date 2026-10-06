"""
5. Count Vowels and Consonants
A language-learning application wants to analyze the characters used in a paragraph.
Write a Python program that reads a file named "paragraph.txt" and counts:
1. Total number of vowels
2. Total number of consonants
Ignore numbers, spaces and special characters.
"""

try:
    with open("paragraph.txt","a") as f:
        text=input("Enter a paragraph: ")
        f.write(text+"\n")

    with open("paragraph.txt","r") as f:
        vowels=0
        consonants=0
        for line in f:
            for char in line:
                if char.isalpha():
                    if char.lower() in "aeiou":
                        vowels+=1
                    else:
                        consonants+=1

        print("Total Vowels:",vowels)
        print("Total Consonants:",consonants)
finally:
    print("Program executed successfully.")