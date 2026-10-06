"""
Count Occurrence of a Particular Word
A company wants to analyze how frequently a particular keyword appears in a document.
Write a Python program that:
1. Reads a file named "article.txt".
2. Accepts a word from the user.
3. Counts how many times the given word occurs in the file.
"""

with open("article2.txt","r") as f:
    word = input("Enter your word to search : ")
    count=0
    for line in f:
        data = line.strip().split()
        for w in data:
            if w == word:
                count +=1 
    print(f"Python Occours {count} times in the file")