""" Банкомат 2.0: переробіть программу з функціонального підходу 
програмування на використання класів. Додайте шанс 10% отримати 
бонус на баланс при створенні нового користувача."""


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

banknotes = [(10, 100), (20, 100), (50, 100), (100, 100), (200, 100), (500, 100), (1000, 100)]
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