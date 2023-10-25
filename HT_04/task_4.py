""" Write a Python program that demonstrates exception chaining. Create a custom 
exception class called CustomError and another called SpecificError. In your program 
(could contain any logic you want), raise a SpecificError, and then catch it in a try/except block, 
re-raise it as a CustomError with the original exception as the cause. 
Display both the custom error message and the original exception message."""

class CustomError(Exception):
    def __init__(self, message="Custom error raised!"):
        super().__init__(message)


class SpecificError(Exception):
    def __init__(self, message="Specific error raised!"):
        super().__init__(message)


try:
    number = input("Enter number: ")
    raise SpecificError
except SpecificError as er:
    try:
        raise CustomError
    except CustomError as e:
        print(f"Error: {e}")    
    print(f"Error: {er}")
