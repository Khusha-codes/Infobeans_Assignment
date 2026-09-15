import uuid

name = input("Enter student name: ")

student_id = str(uuid.uuid4())

print("Student Name:", name)
print("Student ID:", student_id)