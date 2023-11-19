
""" Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів. Якщо в попередньому 
    завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати 
    її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача (при створенні новго 
    користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який 
    матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу 
    що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> 
    повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья 
    баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (не вірний 
    логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)
"""

import sqlite3
from login import login, register_user
from user import user_menu
from incasator import admin_menu


conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        is_incasator INTEGER DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        balance REAL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS banknotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nominal INTEGER UNIQUE NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

banknotes = [(10, 100), (20, 100), (50, 100), (100, 100), (200, 100), (500, 100), (1000, 100)]
cursor.executemany('INSERT OR IGNORE INTO banknotes (nominal, quantity) VALUES (?, ?)', banknotes)
conn.commit()


def main():
    while True:
        print("\nEnter your choice:")
        print("1. Register new user")
        print("2. Login")
        print("3. Quit\n")
        choice = input()

        if choice == '1':
            register_user()
        elif choice == '2':
            username = login() #"andrii" #
            if not username:
                continue
            elif username == "admin":
                admin_menu()
            else:
                user_menu(username)
        elif choice == '3':
            print("\nGoodbye!\n")
            conn.close()
            break
        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main()
