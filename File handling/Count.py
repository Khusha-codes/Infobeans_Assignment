"""
4. Count Lines, Words and Characters in a File
A content management company wants to analyze the size of a text document.
Write a Python program that reads a file named "article.txt" and displays:
1. Total number of lines
2. Total number of words
3. Total number of characters
"""
try:
    line_count=0
    word_count=0
    char_count=0
    with open("article.txt","r") as f:
        for line in f:
            line_count+=1
            word_count+=len(line.split())
            char_count+=len(line)
        print("Total Lines:",line_count)
        print("Total Words:",word_count)
        print("Total Characters:",char_count)
finally:
    print("Done")