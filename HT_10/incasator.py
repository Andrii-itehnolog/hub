import sqlite3


conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


def admin_menu():
    while True:
        print("\nEnter your choice:")
        print("1. View ATM balance")
        print("2. Change ATM balance")
        print("3. Back to previous menu\n")
        choice = input()
        if choice == '1':
            view_atm_balance()
        elif choice == '2':
            change_banknotes_quantity()
        elif choice == '3':
            print("\nLogout successful.\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


def view_atm_balance():
    atm_balance = cursor.execute('SELECT SUM(nominal * quantity) FROM banknotes').fetchone()[0]
    print(f'\nATM balance: {atm_balance:.2f} uah\n')
    cursor.execute('SELECT * FROM banknotes ')
    banknotes = cursor.fetchall()
    for banknote in banknotes:
        print(f"banknote - {banknote[1]} uah; quantity - {banknote[2]}")
    


def change_banknotes_quantity():
    nominal = int(input("Enter the nominal of the banknote: "))
    quantity = int(input("Enter the new quantity: "))
    cursor.execute('UPDATE banknotes SET quantity=? WHERE nominal=?', (quantity, nominal))
    conn.commit()
    print("\nBanknote quantity updated successfully.\n")


def main():
    pass

 
if __name__ == "__main__":
    main()