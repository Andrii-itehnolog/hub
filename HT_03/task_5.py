"""Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary."""

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 5}

temp_list = []
dict_without_duplicates = dict()
for key, value in my_dict.items():
    if value not in temp_list:
        temp_list.append(value)
        dict_without_duplicates[key] = value
print(f'Dictionary without duplicates is:\n{dict_without_duplicates}')
