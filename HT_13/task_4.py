""" 4. Create 'list'-like object, but index starts from 1
and index of 0 raises error. Тобто це повинен бути клас,
який буде поводити себе так, як list (маючи основні методи),
але індексація повинна починатись із 1"""


class MyList:
    def __init__(self):
        self.start_list = []

    def __getitem__(self, index):
        check_index(index)
        return self.start_list[index-1]

    def __setitem__(self, index, value):
        check_index(index)
        if index > len(self.start_list):
            raise IndexError(f"List has only {len(self.start_list)} items!")
        else:
            self.start_list[index-1] = value

    def __len__(self):
        return len(self.start_list)

    def append(self, value):
        self.start_list.append(value)

    def pop(self, index):
        check_index(index)
        return self.start_list.pop(index-1)

    def insert(self, index, value):
        index = check_index(index)
        self.start_list.insert(index-1, value)


def check_index(index):
    if index == 0:
        raise IndexError("List starts from 1!")
    return index


if __name__ == "__main__":
    my_list = MyList()
    for i in range(5):
        my_list.append(i+1)
    print(f"Start list: {my_list.start_list}")
    place = 3
    value = 10
    my_list.insert(place, value)
    print(f"List after inserting {value} on place number {place}: {my_list.start_list}")
    print(f"First element is {my_list[1]}")
    try:
        print("Try to get zero element")
        print(my_list[0])
    except IndexError as e:
        print(e)
    place = 2
    my_list.pop(place)
    print(f"Final list after deleting element number {place}: {my_list.start_list}")


