"""
Find the Most Frequently Used Word

A content-analysis application wants to identify the most frequently used word in an article.

Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.

Input File: article.txt

Python is easy.
Python is powerful.
Python is popular.
Java is also popular.
"""
with open("article04.txt", "w") as f:
    f.write('''Python is easy.
Python is powerful.
Python is popular.
Java is also popular.
            ''')

with open("article04.txt", "r") as f:
    data = f.read()

words = data.split()

max = 0
most = ""

for word in words:
    count = 0
    for w in words:
        if word == w:
            count = count + 1

    if count > max:
        max = count
        most = word

print("Most Frequently Used Word:", most)
print("Frequency:", max)