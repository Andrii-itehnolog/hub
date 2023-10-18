""" 
Write a script which accepts two sequences of comma-separated colors from user. 
Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.
"""

first_input = input("Please, enter first comma-separated colors sequence: ")
first_set_of_colors = set(first_input.split(","))
second_input = input("Please, enter second comma-separated colors sequence: ")
second_set_of_colors = set(second_input.split(","))
print(first_set_of_colors.difference(second_set_of_colors))



