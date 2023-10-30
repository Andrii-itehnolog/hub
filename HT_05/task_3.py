""" 3. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями. 
Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої 
буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює z"""

    
def comparison_two_numbers(x, y):
    if x > y:
        return f"{x} is greater then {y}  by {x - y}"
    elif x < y:
        return f"{y} is greater then {x}  by {y - x}"
    else:
        return f"{x} is equals {y}"


if __name__ == "__main__":
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
            print("Incorrect input!")
    try:
        print(comparison_two_numbers(first_number, second_number))
    except Exception:
        print("Please start again!!")

