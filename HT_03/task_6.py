"""Write a script to get the maximum and minimum value in a dictionary."""

sample_dict = {'foo': '36',
               'bar': [-3],
               'dou': {"value1": 77},
               'USD': 36,
               'AUD': 19.2,
               'name': 99.99,
               'age': 100,
               'baz': [9, 6],
               'test': ("value", 150),
               }
dict_of_lists = {'numbers': [],
                 'strings': [],
                 'lists': [],
                 'tuples': []}
for value in sample_dict.values():
    if isinstance(value, int) or isinstance(value, float):
        dict_of_lists['numbers'].append(value)
    elif isinstance(value, str):
        dict_of_lists['strings'].append(value)
    elif isinstance(value, list):
        dict_of_lists['lists'].append(value)
    elif isinstance(value, tuple):
        dict_of_lists['tuples'].append(value)
for key, elem in dict_of_lists.items():
    if elem:
        print(f"Maximum of {key} is {max(elem)}")
        print(f"Minimum of {key} is {min(elem)}")