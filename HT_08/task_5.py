""" 5. Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих 
регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж 1 раз. 
Рядок буде складатися лише з цифр та букв (великих і малих). Реалізуйте обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі """


def count_chars(input_string):
    input_string = input_string.lower()
    count = sum(1 for char in set(input_string) if input_string.count(char) > 1 and char.isalnum())
    return count


if __name__ == "__main__":
    test = "ABBA"
    result = count_chars(test)
    print(result)
