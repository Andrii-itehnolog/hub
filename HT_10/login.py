import re
import sqlite3


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


conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


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
        return True
    except (UsernameException, PasswordLengthException,PasswordLettersException, PasswordDigitException) as e:
        print(e)
        return False


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        username = cursor.fetchone()
        if username:
            print("\nLogin successful.\n")
            return username[1]
        else:
            print("\nWrong username or password!!!\n")
            return


def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    # if username == "admin":
    #     cursor.execute('INSERT INTO users (username, password, is_incasator) VALUES (?, ?, 1)', (username, password))
    #     conn.commit()
    #     print("Incasator registered successful.")
    #     return True
    if valid_user(username, password):
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("\nRegistration successful.\n")
    else:
        print("\nInvalid username or password format.\n")


def main():
    pass

 
if __name__ == "__main__":
    main()

