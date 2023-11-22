import sqlite3
import datetime
from random import random

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


class UserMenu:

    def all_transactions_log(self, username):
        cursor.execute('SELECT * FROM transactions WHERE user_id=? ', (username,))
        transactions = cursor.fetchall()
        for transaction in transactions:
            print(transaction)

    def check_balance(self, username):
        cursor.execute('SELECT balance FROM transactions WHERE user_id=? ORDER BY id DESC LIMIT 1', (username,))
        balance = cursor.fetchone()
        if balance:
            return balance[0]
        return 0

    def bonus_plus(self, username):
        cursor.execute('SELECT bonus FROM users WHERE username=?', (username,))
        bonus = cursor.fetchone()
        if bonus[0] == 0:
            return 1
        if random() < 0.05:
            print("\nYou are lucky and win additional 10% bonus!!!\n")
            cursor.execute('UPDATE users SET bonus=? WHERE username=?', (0, username))
            conn.commit()
            return 1.1
        else:
            print("\nUnfortunately you didn't win additional bonus:(")
        return 1

    def deposit(self, username):
        try:
            amount = float(input("\nPlease, enter amount of money you want to add to your account: "))
        except ValueError:
            print("\nIncorrect input\n")
            return
        if amount < 0:
            print(f"\nAmount must be greater then zero!!!\n")
            return
        if amount % 10 == 0:
            amount = amount * self.bonus_plus(username)
            cursor.execute('INSERT INTO transactions (user_id, date, type, amount, balance) VALUES (?, ?, ?, ?, ?)',
                           (username, str(datetime.datetime.now()), 'deposit', amount,
                            self.check_balance(username) + amount))
            conn.commit()
            print(f'\nYou added {amount:.2f} uah.\nYour balance is {self.check_balance(username):.2f} uah.\n')
        else:
            rest = amount % 10
            amount -= (amount % 10)
            amount = amount * self.bonus_plus(username)
            cursor.execute('INSERT INTO transactions (user_id, date, type, amount, balance) VALUES (?, ?, ?, ?, ?)',
                           (username, str(datetime.datetime.now()), 'deposit', amount,
                            self.check_balance(username) + amount))
            conn.commit()
            print(f"{amount:.2f} uah have been added to your account. Rest is {rest}.")

    def withdraw(self, username):
        try:
            amount = float(input("\nPlease, enter amount of money you want to withdraw from your account: "))
        except ValueError:
            print("\nIncorrect input\n")
            return
        if amount > self.check_balance(username):
            print(f"\nYou have only {self.check_balance(username):.2f} uah on your account!!!!!!\n")
            return
        elif amount < 0:
            print(f"\nAmount must be greater then zero!!!\n")
            return
        cursor.execute('SELECT SUM(nominal * quantity) FROM banknotes')
        balance_atm = cursor.fetchone()
        if 0 < amount <= self.check_balance(username) and amount <= balance_atm[0]:
            cursor.execute('INSERT INTO transactions (user_id, date, type, amount, balance) VALUES (?, ?, ?, ?, ?)',
                           (username, str(datetime.datetime.now()), 'withdraw', amount,
                            self.check_balance(username) - amount))
            conn.commit()
            print(f'\nYou withdrawn {amount:.2f} uah.\nYour balance is {self.check_balance(username):.2f} uah.\n')
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def user_menu(self, username):
        while True:
            print("\nEnter your choice:")
            print("1. Check balance")
            print("2. Add money")
            print("3. Withdraw money")
            print("4. Check transactions")
            print("5. Back to previous menu\n")
            choice = input()
            if choice == "1":
                print(f"\nYour balance is {self.check_balance(username)} uah\n")
            elif choice == "2":
                self.deposit(username)
            elif choice == "3":
                self.withdraw(username)
            elif choice == "4":
                self.all_transactions_log(username)
            elif choice == "5":
                break
            else:
                print("\nWrong choice. Try one more time.\n")


def main():
    pass


if __name__ == "__main__":
    main()
