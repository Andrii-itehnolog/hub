
""" Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  
kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> змінити регістер всіх букв на протилежний та вивести нову строку з літер в зворотноьому 
   порядку; замінити кожну цифру на (10 - цифра) і вивести їх суму"""

import string


def converting_line(line):
    line_of_letters = ""
    sum_of_digits = 0
    for elem in line:
        if elem in string.ascii_letters:
            line_of_letters += elem.swapcase()
        elif elem in string.digits:
            sum_of_digits += 10 - int(elem)
    return f"The sum of numbers in line is {sum_of_digits}. New line of letters is:  {line_of_letters[::-1]}"


def count_characters(line):
    digit_count = 0
    letters_count = 0
    for elem in line:
        if elem in string.ascii_letters:
            letters_count += 1
        elif elem in string.digits:
            digit_count += 1
    return f"Length of line is {len(line)}. Quantity of digits is {digit_count}, quantity of letters is {letters_count}"


def sum_and_letters(line):
    line_of_letters = ""
    sum_of_digit = 0
    for elem in line:
        if elem in string.ascii_letters:
            line_of_letters += elem
        elif elem in string.digits:
            sum_of_digit += int(elem)
    return f"The sum of numbers in line is {sum_of_digit}. New line of letters is:  {line_of_letters}"


def line_checking(line):
    if 30 <= len(line) <= 50:
        return count_characters(line)
    elif len(line) < 30:
        return sum_and_letters(line)
    else:
        return converting_line(line)


if __name__ == "__main__":
    # line = "f98A5eToi4nr 0c3n3.0FGn03ien3c{0rfe kVWM400w<enGDBSwe00ko/ijn35pijGp4b6]ij7k5j78p3kj546p'4 " \
    #        "65jnASDoj35pF6j345"
    line = input("Please enter the line of characters: ")
    print(line_checking(line))
