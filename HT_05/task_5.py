""" 5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя, яка 
б приймала 3 аргументи - один з яких операцiя, яку зробити! Аргументи брати від юзера 
(можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2). Операції що мають бути 
присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!"""


def addition(number1, number2):
    return f"The result of addition two numbers is: {number1 + number2}"


def subtraction(number1, number2):
    return f"The result of subtraction two numbers is: {number1 + number2}"


def multiplication(number1, number2):
    return f"The result of multiplication two numbers is: {number1 * number2}"


def division(number1, number2):
    try:
        result = number1 / number2
        return f"The result of division two numbers is: {result}"
    except ZeroDivisionError:
        return "Second number can't be zero!"


def modulus(number1, number2):
    try:
        result = number1 % number2
        return f"The result of modulus two numbers is:  {result}"
    except ZeroDivisionError:
        return "Second number can't be zero!"


def exponentiation(number1, number2):
    return f"The result of exponentiation two numbers is: {number1 ** number2}"


def floor_division(number1, number2):
    try:
        result = number1 // number2
        return f"The result of floor_division two numbers is:  {result}"
    except ZeroDivisionError:
        return "Second number can't be zero!"


def calculation(number_1, number_2, operand):
    operation = {"+": addition(number_1, number_2),
                 "-": subtraction(number_1, number_2),
                 "*": multiplication(number_1, number_2),
                 "/": division(number_1, number_2),
                 "%": modulus(number_1, number_2),
                 "**": exponentiation(number_1, number_2),
                 "//": floor_division(number_1, number_2)
                 }
    if operand in operation:
        return operation[operand]
    else:
        return "Wrong choice!"


if __name__ == "__main__":
    number_1 = input("Please enter first number: ")
    number_2 = input("Please enter second number: ")
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        try:
            number_1 = float(number_1)
            number_2 = float(number_2)
        except ValueError:
            print("Incorrect input!")
    print("""
    Please select an operation:
    +  for addition
    -  for subtraction
    *  for multiplication
    /  for division
    % for modulus
    ** for exponentiation
    // floor_division""")
    operand = input("Enter your choice(+ , - , * , / , % , ** ,  //): ")

    print(calculation(number_1, number_2, operand.strip()))
