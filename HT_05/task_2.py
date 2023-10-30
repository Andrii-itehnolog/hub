""" 2. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь 
результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, 
яка всередині викликає 3 попереднi, обробляє їх результат та також повертає результат своєї роботи. 
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3."""


def checking_is_number(number):
    try:
        number = int(number)
    except ValueError:
        try:
            number = float(number)
        except ValueError:
            print("Input is not a number!!!")
        else:
            return number
    else:
        return number


def area_of_square(number):
    return number ** 2
    

def user_input():
    number = input("Please enter number: ")
    return number


def format_output():
    try:
        number = user_input()
        number = checking_is_number(number)
        area = area_of_square(number)
    except TypeError:
        return f"Please start again!!"
    return f"Area of square with side {number} is {area}"


if __name__ == "__main__":
    print(format_output())
