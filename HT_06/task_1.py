""" 1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата, 
і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ."""


def square(side):
    if side > 0:
        area_of_square = side ** 2
        perimeter_of_square = side * 4
        diagonal_of_square = round(side * 2 ** (1/2), 2)
        return perimeter_of_square, area_of_square, diagonal_of_square
    else:
        return f"Side must be positive number!"

if __name__ == "__main__":
    side = input("Please enter the size of squares side:  ")
    try:
        side = int(side)
    except ValueError:
        try:
            side = float(side)
        except ValueError:
            print("Input is not a number!!!")
            exit()
    print(f"Perimeter, area and diagonal of square with side {side} are: {square(side)}")