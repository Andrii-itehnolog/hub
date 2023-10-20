"""Write a script to get the maximum and minimum value in a dictionary."""

import random

length_of_dict = random.randint(10, 20)
dict_of_numbers = dict()
for i in range(length_of_dict):
    dict_of_numbers[i] = random.randint(0, 1000)
print(dict_of_numbers)
print(f"Maximum value of dict is: {max(dict_of_numbers.values())}")
print(f"Minimum value of dict is: {min(dict_of_numbers.values())}")


