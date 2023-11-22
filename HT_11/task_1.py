""" 1. Створити клас Calc, який буде мати атребут last_result та 4 методи. 
Методи повинні виконувати математичні операції з 2-ма числами, а саме 
додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result 
він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повенен повернути 
результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6"""


class Calc:

    def __init__(self):
        self.last_result = None
        self.previous_result = None

    def addition(self, first_number, second_number):
        result = first_number + second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result

    def subtraction(self, first_number, second_number):
        result = first_number - second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result

    def multiplication(self, first_number, second_number):
        result = first_number * second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result

    def division(self, first_number, second_number):
        try:
            result = first_number / second_number
            self.last_result = self.previous_result
            self.previous_result = result
            return result
        except ZeroDivisionError:
            self.last_result = self.previous_result
            self.previous_result = None
            return None


calculator = Calc()
print(calculator.last_result)

calculator.addition(1, 1)
print(calculator.last_result)

calculator.multiplication(2, 3)
print(calculator.last_result)

calculator.subtraction(16, 4)
print(calculator.last_result)

calculator.addition(6, 1)
print(calculator.last_result)

calculator.multiplication(8, 3)
print(calculator.last_result)

calculator.division(25, 5)
print(calculator.last_result)

calculator1 = Calc()
print(calculator1.last_result)

calculator1.addition(6, 1)
print(calculator1.last_result)

calculator1.multiplication(8, 3)
print(calculator1.last_result)

calculator1.subtraction(25, 5)
print(calculator1.last_result)