""" Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
Кожне введене значення спочатку пробує перевести в int. У разі помилки - пробує перевести в float,
а якщо і там ловить помилку - пропонує ввести значення ще раз (зручніше на даному етапі навчання
для цього використати цикл while) Виводить результат ділення першого на друге. Якщо при цьому виникає
помилка - оброблює її і виводить відповідне повідомлення"""


while True:
    first_number = input("Please enter first number: ")
    second_number = input("Please enter second number: ")
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        try:
            first_number = float(first_number)
            second_number = float(second_number)
        except ValueError:
            print("Incorrect input! Please try again!")
        else:
            break
    else:
        break

try:
    result = first_number / second_number
except ZeroDivisionError:
    print("Division by zero! Incorrect second number!")
else:
    print(f"Result of dividing {first_number} by {second_number} is {result}")
