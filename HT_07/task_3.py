"""3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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
    if re.search(r".*[A-Z]+[a-z]+.*", password):
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
        return f"Name: {username}\nPassword: {password}\nStatus: OK"
    except (UsernameException, PasswordLengthException,PasswordLettersException, PasswordDigitException) as e:
        return f"Name: {username}\nPassword: {password}\nStatus: {e}"

    
if __name__ == "__main__":
   user_dict = {
        "Andrii": "Password1",
        "Serhii": "Password",
        "Ol": "Password_3",
        "Kateryna": "password4",
        "Olena": "PASSWORD5"
    }
   for username, password in user_dict.items(): 
      print(valid_user(username, password))

      