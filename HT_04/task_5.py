""" Create a Python program that repeatedly prompts the user for a number until a valid integer is provided. 
Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid 
integer is entered. Display the final valid integer."""


while True:
    try:
        number = int(input("Please enter integer number: "))
    except ValueError:
        print("Incorrect input! Please try again!")
    else:
        break
print(f"Valid number is: {number}")
