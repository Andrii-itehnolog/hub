
""" Наприклад маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfe  
kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345" -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> змінити регістер всіх букв на протилежний та вивести нову строку з літер в зворотноьому 
   порядку; замінити кожну цифру на (10 - цифра) і вивести їх суму"""


def converting_line(letters_string, digit_string):
    sum_of_digit = 0
    for char in digit_string:
        sum_of_digit += (10 - int(char))
    return f"The sum of numbers in line is {sum_of_digit}. New line of letters is:  {letters_string[::-1].swapcase()}"


def count_characters(letters_string, digit_string, length):
    return f"Length of line is {length}. Quantity of digits is {len(digit_string)}, quantity of letters is {len(letters_string)}"


def sum_and_letters(letters_string, digit_string):
    sum_of_digit = 0
    for char in digit_string:
        sum_of_digit += int(char)
    return f"The sum of numbers in line is {sum_of_digit}. New line of letters is: {letters_string}"


def line_checking(letters_string, digit_string, length):
    if 30 <= length <= 50:
        return count_characters(letters_string, digit_string, length)
    elif length < 30:
        return sum_and_letters(letters_string, digit_string)
    else:
        return converting_line(letters_string, digit_string)


if __name__ == "__main__":
    # line = "f98A5eToi4nr 0c3n3.0FGn03ien3c{0rfe kVWM400w<enGDBSwe00ko/ijn35pijGp4b6]ij7k5j78p3kj546p'4 " \
    #        "65jnASDoj35pF6j345"
    line = input("Please enter the line of characters: ")
    digit_string = ""
    letters_string = ""
    for elem in line:
        if elem.isalpha():
            letters_string += elem
        elif elem.isdigit():
            digit_string += elem 
    print(line_checking(letters_string, digit_string, len(line)))

