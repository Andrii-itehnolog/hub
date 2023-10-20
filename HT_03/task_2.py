""" Write a script to remove an empty elements from a list.
    Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
"""

test_list= [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
new_list = []
for i in test_list:
    if i:
        new_list.append(i)
print(f'New list is:\n{new_list}')


