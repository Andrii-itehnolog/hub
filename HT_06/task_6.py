""" 6. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
Тобто функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - 
пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]"""


def shift_func(data_list, shift):
    data_list = data_list[-shift:] + data_list[:-shift]
    return data_list


if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5, 6, 7]
    print(shift_func(example_list, shift=2))  
    print(shift_func(example_list, shift=-3))  
