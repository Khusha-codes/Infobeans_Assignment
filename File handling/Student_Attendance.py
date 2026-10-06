'''A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:

RollNo,StudentName,Status

where Status is either Present or Absent.


Write a Python program to:

Accept attendance details for N students.
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage'''

try :
    n = int(input("Enter number of student: "))
    for i in range(n):
        roll = input("Enter Student roll no.: ") + " "
        name = input("Enter Student name: ") + " "
        status = input("Enter Status: ") 
        with open("Attendance.txt","a") as f :
            f.write(f"{roll} {name} {status}\n")
    P_student = 0
    with open("Attendance.txt","r") as f :
        for l in f:
            line = l.strip().split()
            if line[2] == "Present":
                P_student += 1
    print("Total Student: ",n)
    print("Present Students: ",P_student)
    print("Absent Students: ",n - P_student)
    print("Attendance Percentage: ",(P_student/n)*100,"%")
finally:
    print("Done")