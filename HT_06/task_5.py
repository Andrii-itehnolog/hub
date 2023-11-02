""" 5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить 
всі числа Фібоначчі, що не перевищують його."""


def fibonacci(number):
    a, b = 0, 1
    list_of_fibonacci = []
    while a <= number:
        list_of_fibonacci.append(a)
        a, b = b, a + b
    return list_of_fibonacci


if __name__ == "__main__":
    try:
        number = int(input("Please enter number: "))
        print(fibonacci(number))
    except ValueError:
        print("Number must be only integer")
    