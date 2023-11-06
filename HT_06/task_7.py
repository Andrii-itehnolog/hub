""" 7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових 
елементів у ньомy і виводить результат. Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1" """


def count_elements(input_data):
    dict_of_elements = {}
    for element in input_data:
        if isinstance(element, ( list, dict )):
            key = str(element)
            if key in dict_of_elements:
                dict_of_elements[key] += 1
            else:
                dict_of_elements[key] = 1
        else:
            if element in dict_of_elements:
                dict_of_elements[element] += 1
            else:
                dict_of_elements[element] = 1

    for key, value in dict_of_elements.items():
        print(f"Element {key} is present {value} times.")


if __name__ == "__main__":
    example_list = [1, 1, 'foo', [1, 2], "None", True, 2.6, 'foo', "1", [1, 2], 5, "gg", False, (2, 3), 2.6, "False", (2, 3),"True", None ,  {1: "test"}, 0 , False]
    count_elements(tuple(example_list))
