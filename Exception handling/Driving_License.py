'''DRIVING LICENSE REGISTRATION

Scenario:
A government driving license registration system needs to validate whether
a person is eligible to apply for a driving license.

Create the following custom exceptions:

1. InvalidAgeForDrivingLicenseException
2. InvalidMarkForDrivingLicenseException

## Eligibility Rules:

1. Age must be greater than or equal to 18.
2. Age cannot be negative.
3. Road rules test marks must be between 0 and 100.
4. A person must score more than 80 marks to pass the test.

## Requirements:

1. Create the Person class with the following attributes:

   name
   age
   mark

2. Create the two custom exception classes.

3. Create a method named check_eligibility().

4. Validate age first.

5. If age is negative, raise:

   InvalidAgeForDrivingLicenseException: Invalid age

6. If age is less than 18, raise:

   InvalidAgeForDrivingLicenseException:
   Age should be more than 18 years old

7. Validate marks.

8. If marks are negative or greater than 100, raise:

   InvalidMarkForDrivingLicenseException: Invalid mark

9. If marks are 80 or less, raise:

   InvalidMarkForDrivingLicenseException:
   Mark should be more than 80

10. If all conditions are satisfied, display:

    Approved

11. Handle all exceptions using try-except.
'''

class InvalidAgeForDrivingLicenseException(Exception):
        pass

class InvalidMarkForDrivingLicenseException(Exception):
     pass

class Person:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark

    def check_eligibility(self):
      if self.age < 0:
         raise InvalidAgeForDrivingLicenseException("Invalid age")
      elif self.age < 18:
         raise InvalidAgeForDrivingLicenseException("Age should be more than 18 years old")
      if self.marks > 100 or self.marks < 0:
         raise InvalidMarkForDrivingLicenseException("Invalid mark")
      elif self.marks < 80:
         raise InvalidMarkForDrivingLicenseException("Mark should be more than 80")

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
p = Person(name,age,marks)

try:
     p.check_eligibility()
except Exception as e:
     print(e)
else:
     print("Approved")