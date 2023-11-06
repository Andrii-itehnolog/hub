""" 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль). 
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - 
необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його також треба створити =))"""


class LoginException(Exception):
    def __init__(self, message="Incorrect username or password!"):
        super().__init__(message)


def check_password(username, password, silent=False):
    user_dict = {
        "Andrii": "Password_1",
        "Serhii": "Password_2",
        "Oleg": "Password_3",
        "Kateryna": "Password_4",
        "Olena": "Password_5"
    }
    try:
        if username in  user_dict .keys() and password == user_dict[username]:
            return True
        elif silent:
            return False
        else:
            raise LoginException()
    except LoginException as e:
        return e
    

if __name__ == "__main__":
    print(check_password("Andrii", "Password_1", True))
    print(check_password("Andri", "Password_1", True))
    print(check_password("Andrii", "Password_2", True))
    print(check_password("Andri", "Password_1"))

