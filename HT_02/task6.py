"""  Write a script to check whether a value from user input is contained in a group of values.
    e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
         [1, 2, 'u', 'a', 4, True] --> 5 --> False
"""

group = [1,  2,  'u',  'a ',  4,  True]
user_input = input("Please enter your value: ")
if user_input.isnumeric():
    user_input = int(user_input)
if user_input in group:
    print(True)
else:
    print(False)



