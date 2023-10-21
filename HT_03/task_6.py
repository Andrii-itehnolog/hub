"""Write a script to get the maximum and minimum value in a dictionary."""


def maximum_of_list(list_of_elements):
    if list_of_elements:
        return max(list_of_elements)
    else:
        return 'not found'


def minimum_of_list(list_of_elements):
    if list_of_elements:
        return min(list_of_elements)
    else:
        return 'not found'


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
max_lists = [[], [], [], []]
names_of_lists = ['numbers', 'strings', 'lists', 'tuples']
for value in sample_dict.values():
    if type(value) == int or type(value) == float:
        max_lists[0].append(value)
    elif type(value) == str:
        max_lists[1].append(value)
    elif type(value) == list:
        max_lists[2].append(value)
    elif type(value) == tuple:
        max_lists[3].append(value)
count = 0
for elem in max_lists:
    print(f"Maximum of {names_of_lists[count]} is {maximum_of_list(elem)}")
    print(f"Minimum of {names_of_lists[count]} is {minimum_of_list(elem)}")
    count += 1