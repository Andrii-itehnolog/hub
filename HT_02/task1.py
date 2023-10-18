""" 
Write a script which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers.
"""

user_input = input("Please, enter comma-separated numbers: ")
new_list = user_input.split(",")
new_tuple = tuple(new_list)

