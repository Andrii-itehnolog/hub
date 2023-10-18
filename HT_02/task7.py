"""  Write a script to concatenate all elements in a list into a string and print it. List must be include 
both strings and integers and must be hardcoded.
"""

mixed_list = [123,  256,  'user',  'student',  458]
concatenated_list = ""
for item in mixed_list:
    concatenated_list += str(item)
print(concatenated_list)
