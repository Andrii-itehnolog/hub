""" 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   - пароль повинен містити хоча б одну велику та одну маленьку літери 
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
   """


import re


class UsernameException(Exception):
    def __init__(self, message="Incorrect username length!!!"):
        super().__init__(message)


class PasswordLengthException(Exception):
    def __init__(self, message="Incorrect passwords length!!!"):
        super().__init__(message)


class PasswordLettersException(Exception):
    def __init__(self, message="The password must contain at least one lowercase and one uppercase letter!!!"):
        super().__init__(message)


class PasswordDigitException(Exception):
    def __init__(self, message="The password must contain at least one number!!!"):
        super().__init__(message)


def valid_username(username):
    if 3 <= len(username) <= 50:
        return True
    else:
        raise UsernameException()


def valid_password_digit(password):
    if re.search(r".*\d+.*", password):
        return True
    else:
        raise PasswordDigitException()


def valid_password_letters(password):
    if re.search(r"(?=.*[a-z])(?=.*[A-Z])", password):
        return True
    else:
        raise PasswordLettersException()


def valid_password_length(password):
    if len(password) >= 8:
        return True
    else:
        raise PasswordLengthException()


def valid_user(username, password):
    try:
        valid_username(username)
        valid_password_digit(password)
        valid_password_letters(password)
        valid_password_length(password)
        return f"Username and password are valid!"
    except (UsernameException, PasswordLengthException,PasswordLettersException, PasswordDigitException) as e:
        return e

    
if __name__ == "__main__":
    username =  input("Please enter username: ")
    password =  input("Please enter password: ")
    print(valid_user(username, password))


