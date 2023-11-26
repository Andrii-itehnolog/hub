import sqlite3

conn = sqlite3.connect("atm.db")
cursor = conn.cursor()


class WithdrawMoney:
    def __init__(self):
        self.available_banknotes = self.load_banknotes_from_db()
        self.min_combination = None
        self.current_combination = None

    def load_banknotes_from_db(self):
        cursor.execute("SELECT nominal, quantity FROM banknotes")
        banknotes_data = cursor.fetchall()
        banknotes = {}
        for nominal, quantity in banknotes_data:
            banknotes[nominal] = quantity
        return banknotes

    def withdraw_money(self, amount, start_index=0):
        if self.current_combination is None:
            self.current_combination = {}
        if amount == 0:
            self.update_min_combination()
            return

        for i in range(start_index, len(self.available_banknotes)):
            banknote = list(self.available_banknotes.keys())[i]
            if self.available_banknotes[banknote] > 0 and banknote <= amount:
                self.current_combination[banknote] = self.current_combination.get(banknote, 0) + 1
                self.available_banknotes[banknote] -= 1

                self.withdraw_money(amount - banknote, i)

                self.current_combination[banknote] -= 1
                self.available_banknotes[banknote] += 1

    def update_banknotes(self):
        for banknote, quantity in self.min_combination.items():
            cursor.execute("UPDATE banknotes SET quantity = quantity - ? WHERE nominal = ?", (quantity, banknote))
        conn.commit()

    def update_min_combination(self):
        if self.min_combination is None or len(self.current_combination) < len(self.min_combination):
            self.min_combination = self.current_combination.copy()

    def print_min_combination(self):
        if self.min_combination:
            print(f"\nYour bills: {self.min_combination}\n")
            self.update_banknotes()
        else:
            print("No valid combination found.")


def main():
    pass


if __name__ == "__main__":
    main()