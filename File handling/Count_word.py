"""
Count Words Starting With a Particular Letter

A search engine wants to analyze words beginning with a particular character.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.

Input File: article.txt

Python programming provides powerful features.
Programming helps developers build applications.
"""
with open("article2.txt","r") as f:
    count=0
    ch = input("Enter Character : ")
    for line in f:
        data = line.strip().split()
        for w in data:
            if w.startswith(ch):
                count+=1
    print(f"Words starting with {ch} : ",count)