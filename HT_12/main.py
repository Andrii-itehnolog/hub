""" HT #12
Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр. 
Наприклад: 2560 --> 2х1000, 1х500, 3х20. Будьте обережні з "жадібним алгоритмом"!"""


import sqlite3
from login import UserLogin
from user import UserMenu
from incasator import AdminMenu


conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        bonus INTEGER DEFAULT 1,
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

banknotes = [(1000, 100), (500, 100), (200, 100), (100, 100), (50, 100), (20, 100), (10, 100)]
cursor.executemany('INSERT OR IGNORE INTO banknotes (nominal, quantity) VALUES (?, ?)', banknotes)
conn.commit()


def main():
    user = UserLogin()
    admin = AdminMenu()
    customer = UserMenu()
    while True:
        print("\nEnter your choice:")
        print("1. Register new user")
        print("2. Login")
        print("3. Quit\n")
        choice = input()

        if choice == '1':
            user.register_user()
        elif choice == '2':
            username = user.login()
            if not username:
                continue
            elif username == "admin":
                admin.admin_menu()
            else:
                customer.user_menu(username)
        elif choice == '3':
            print("\nGoodbye!\n")
            conn.close()
            break
        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main()