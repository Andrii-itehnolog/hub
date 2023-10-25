""" Create a Python script that takes an age as input. If the age is less than 18 or greater than 120, raise a custom 
exception called InvalidAgeError. Handle the InvalidAgeError by displaying an appropriate error message."""


class InvalidAgeError(Exception):
    def __init__(self, message="Invalid age!"):
        super().__init__(message)


try:
    age = int(input("Enter your age: "))
    if age < 18 or age > 120:
        raise InvalidAgeError
except ValueError:
    print("Incorrect value entered")
except InvalidAgeError as e:
    print(e)
else:
    print("Your age is correct!")
