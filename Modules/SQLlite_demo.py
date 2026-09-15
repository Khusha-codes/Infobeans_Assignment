import sqlite3

connection = sqlite3.connect("student.db")

print("Database connected")

connection.close()