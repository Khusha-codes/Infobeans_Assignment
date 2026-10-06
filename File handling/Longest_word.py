"""
A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

"""
with open("article1.txt","r") as f:
    l_word=""
    for line in f:
      a = line.strip().split()
      for word in a:
         if len(word) > len(l_word):
            l_word = word
    print("Longest Word : ",l_word)
    print("Length Word : ",len(l_word))