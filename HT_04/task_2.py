""" Create a custom exception class called NegativeValueError. Write a Python program that 
takes an integer as input and raises the NegativeValueError if the input is negative. 
Handle this custom exception with a try/except block and display an error message."""


class NegativeValueError(Exception):
        def __init__(self, message="Number is negative!"):
            super().__init__(message)


try:
    number = int(input("Please enter number: "))
    if number < 0:
        raise NegativeValueError
except NegativeValueError as e:
    print(f"Finding an error:\n {e}")
else:
    print("Entered number is positive!")
