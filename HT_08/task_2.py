""" 2. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), 
сума цифр кожного елемент якого буде дорівнювати 10.
   Результат: [19, 28, 37, 46, 55, 64, 73, 82, 91]"""


if __name__ == "__main__":
    new_list = [i for i in range(0, 100) if sum(int(digit) for digit in str(i)) == 10]
    print(new_list)

    