
"""3. Програма-банкомат. Використувуючи функції створити програму з наступним функціоналом: 
- підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>); 
- кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій 
(файл <{username_transactions.JSON>); 
- є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри; 
знімається не більше, ніж є на рахунку і т.д.). 
Особливості реалізації: 
- файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом); 
- файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла; 
- файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання 
нового користувача - не стримуйте себе :) 
Особливості функціонала: 
- за кожен функціонал відповідає окрема функція; 
- основна функція - <start()> - буде в собі містити весь workflow банкомата: 
- на початку роботи - логін користувача (програма запитує ім'я/пароль). 
Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже 
закінчити роботу - все на ентузіазмі :)) 
- потім - елементарне меню типн: 
Введіть дію: 
1. Продивитись баланс 
2. Поповнити баланс 
3. Вихід 
- далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути 
повністю реалізоване :) 
P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно) 
P.S.S. Добре продумайте структуру програми та функцій (edited) """


import csv
import json
import os
import datetime


def login():
    username = input("Please, enter username: ")
    password = input("Please, enter password: ")
    with open("users.csv") as file:
        data = csv.DictReader(file)
        for row in data:
            if username == row["name"] and password == row["password"]:
                return username
    print("Wrong username or password!!!")
    exit()
 
    
def transactions_log(username, transaction, amount, date ):
    data = {"date": date, "type": transaction, "amount": amount, "balance": check_balance(username)}
    if os.path.exists(f"{username}_transactions.json"):
        with open(f"{username}_transactions.json", "r") as file:
            json_data = json.load(file)
        json_data.append(data)
    else:
        json_data = [data]
    with open(f"{username}_transactions.json", "w") as file:
        json.dump(json_data, file, indent=0)
    

def all_transactions_log(username):
    with open(f"{username}_transactions.json", "r") as file:
        data = json.load(file)
    print(data)

    
def check_balance(username):
    with open(f"{username}_balance.txt") as file:
        balance = float(file.readline())
    return balance


def deposit(username):
    try:
        amount = float(input("\nPlease, enter amount of money you want to add to your account: "))
    except ValueError:
        print("Incorrect input\n")
        return
    balance = check_balance(username) + amount
    with open(f"{username}_balance.txt", "w") as file:
        file.write(str(balance))
    transactions_log(username, "deposit", amount, str(datetime.datetime.now()))
    print(f"\nYou added {amount:.2f} uah.\nYour balance is {check_balance(username):.2f} uah\n")


def withdraw(username):
    try:
        amount = float(input("\nPlease, enter amount of money you want to withdraw from your account: "))
    except ValueError:
        print("Incorrect input\n")
        return
    if amount > check_balance(username):
        print(f"You have only {check_balance(username):.2f} uah on your acount!!!!!!\n")
        return
    balance = check_balance(username) - amount
    with open(f"{username}_balance.txt", "w") as file:
        file.write(str(balance))
    transactions_log(username, "withdraw", amount, str(datetime.datetime.now()))
    print(f"\nYou withdrawn {amount:.2f} uah.\nYour balance is {check_balance(username):.2f} uah\n")


def start():
    username = login()
    while True:
        print("\nEnter your choice:")
        print("1. Check balance")
        print("2. Add money")
        print("3. Withdraw money")
        print("4. Check transactions")
        print("5. Quit\n")
        choice = input()
        if choice == "1":
            print(f"\nYour balance is {check_balance(username):.2f} uah\n")
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            all_transactions_log(username)
        elif choice == "5":
            print("\nGood bye!!")
            break
        else:
            print("\nWrong choice. Try one more time.\n")


if __name__ == "__main__":
    start()
