""" Write a script that will run through a list of tuples and replace the last value for each tuple. 
The list of tuples can be hardcoded. The "replacement" value is entered by user. 
The number of elements in the tuples must be different.
"""

list_of_tuples = [(), (1, 2, 3), ('a', 'b', 'c', 'd'), (2.3, 3.6, 8.3, 5.8, 9.7, 10.0)]

value_for_replacement = input("Please enter value for replacement: ")
counter = 0
for i in list_of_tuples:
    if i:
        temp_list = list(i)
        temp_list[len(temp_list) - 1] = value_for_replacement
        list_of_tuples[counter] = tuple(temp_list)
    counter += 1
print(f'New list of tuples is:\n{list_of_tuples}')


