"""2. Написати функцію, яка приймає два параметри: 
ім'я (шлях) файлу та кількість символів. Файл також додайте в репозиторій. 
На екран повинен вивестись список із трьома блоками - символи з початку, 
із середини та з кінця файлу. Кількість символів в блоках - та, яка введена 
в другому параметрі. Придумайте самі, як обробляти помилку, наприклад, 
коли кількість символів більша, ніж є в файлі або, наприклад, файл із двох 
символів і треба вивести по одному символу, то що виводити на місці середнього 
блоку символів?). Не забудьте додати перевірку чи файл існує
В репозиторій додайте і ті файли, по яким робили тести.
Як визначати середину файлу (з якої брать необхідні символи) - кількість символів 
поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і 
взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - 
дивіться на свій розсуд.
Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр

   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр
"""


class WrongQuantity(Exception):
    pass


def show_symbols(file_path, quantity):
    try:
        with open(file_path) as f:
            data = f.read()
        if len(data) < quantity * 3:
            raise WrongQuantity()
        half_index = len(data) // 2
        if quantity % 2 == 0:
            result = [data[:quantity], data[half_index - quantity // 2: half_index + quantity // 2], data[-quantity:]]
        else:
            result = [data[:quantity], data[half_index - quantity // 2: half_index + quantity // 2 + 1], data[-quantity:]]
        return result

    except FileNotFoundError:
        return f"File not found!!!"
    except WrongQuantity:
        return f"File doesn't have enough symbols!"


if __name__ == "__main__":
    try:
        quantity = int(input("Please enter quantity of chars: "))
    except ValueError:
        print("Quantity must be only integer!!!")
        exit()
    result = show_symbols("test2.txt", quantity)
    print(result)


    