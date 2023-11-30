"""2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної
 бібліотеки (включіть фантазію). Наприклад вона може містити класи Person, 
 Teacher, Student, Book, Shelf, Author, Category і.т.д. """


import sqlite3
import datetime

conn = sqlite3.connect("lib.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS persons (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    page_count INTEGER,
    available INTEGER DEFAULT 1
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS borrowed_books (
    person_id INTEGER,
    book_id INTEGER,
    return_date DATE,
    FOREIGN KEY (person_id) REFERENCES persons(person_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    PRIMARY KEY (person_id, book_id)
)
""")


class Login:

    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            cursor.execute('SELECT * FROM persons WHERE username=? AND password=?', (username, password))
            username = cursor.fetchone()
            if username:
                print("\nLogin successful.\n")
                return username[1]
            else:
                print("\nWrong username or password!!!\n")
                return


class Person:

    def all_available_books(self):
        cursor.execute('SELECT books.* FROM books LEFT JOIN borrowed_books ON books.book_id = borrowed_books.book_id '
                       'WHERE borrowed_books.book_id IS NULL')
        books = cursor.fetchall()
        print('book_id, title, author, genre, quanty of pages, available')
        for book in books:
            print(book)
        return books

    def borrow_book(self, person_id, return_date=datetime.datetime.now() + datetime.timedelta(days=31)):
        self.all_available_books()
        try:
            book_id = int(input("Please enter book_id you want to borrow: "))
        except ValueError:
            print("\nBook_id must be integer!\n")
            return
        cursor.execute('UPDATE books SET available = 0 WHERE book_id = ?', (book_id,))
        cursor.execute('INSERT INTO borrowed_books (person_id, book_id, return_date) ' 
                       'VALUES (?, ?, ?)', (person_id, book_id, return_date))
        conn.commit()
        cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id, ))
        book = cursor.fetchone()
        print(f"\nYou borrowed {book} successfully.\n")

    def return_book(self, person_id):
        self.view_books(person_id)
        try:
            book_id = int(input("Please enter book_id you want to return: "))
        except ValueError:
            print("\nBook_id must be integer\n!")
            return
        cursor.execute('DELETE FROM borrowed_books WHERE person_id = ? AND book_id = ? ', (person_id, book_id))
        cursor.execute("UPDATE books SET available = 1 WHERE book_id = ?", (book_id,))
        conn.commit()
        cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
        book = cursor.fetchone()
        print(f"\nYou returned {book} successfully.\n")

    def view_books(self, person_id):
        cursor.execute('SELECT * FROM books JOIN borrowed_books ON books.book_id = borrowed_books.book_id WHERE '
                       'borrowed_books.person_id = ?', (person_id,))
        books = cursor.fetchall()

        print(books)

    def menu(self, username):
        while True:
            print("\nEnter your choice:")
            print("1. Borrow book")
            print("2. Return book")
            print("3. View available books")
            print("4. List of my books")
            print("5. Back to previous menu\n")
            choice = input()
            if choice == "1":
                self.borrow_book(username)
            elif choice == "2":
                self.return_book(username)
            elif choice == '3':
                self.all_available_books()
            elif choice == "4":
                self.view_books(username)
            elif choice == "5":
                break
            else:
                print("\nWrong choice. Try one more time.\n")


class Librarian(Person):
    def __init__(self):
        super().__init__()

    def add_book(self):
        title = input("Enter title of the book: ")
        author = input("Enter author of the book: ")
        genre = input("Enter genre of the book name: ")
        page_count = input("Enter quantity of the book pages: ")
        cursor.execute('INSERT INTO books (title, author, genre, page_count) '
        'VALUES (?, ?, ?, ?)', (title, author, genre, page_count))
        conn.commit()

    def all_books(self):
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        print('book_id, title, author, genre, quanty of pages, available')
        for book in books:
            print(book)
        return books

    def del_book(self):
        self.all_available_books()
        try:
            book_id = int(input("\nPlease enter book_id you want to delete: "))
        except ValueError:
            print("\nBook_id must be integer!\n")
            return
        cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id, ))
        conn.commit()

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter surname: ")
        cursor.execute('INSERT INTO persons (username, password, first_name, last_name) VALUES (?, ?, ?, ?)',
                       (username, password, first_name, last_name))
        conn.commit()
        print("\nRegistration successful.\n")

    def menu(self, username="admin"):
        while True:
            print("\nEnter your choice:")
            print("1. List of available books")
            print("2. List of all books")
            print("3. Add book")
            print("4. Delete book")
            print("5. Register user")
            print("6. Back to previous menu\n")
            choice = input()
            if choice == '1':
                self.all_available_books()
            elif choice == '2':
                self.all_books()
            elif choice == '3':
                self.add_book()
            elif choice == '4':
                self.del_book()
            elif choice == '5':
                self.register_user()
            elif choice == '6':
                print("\nLogout successful.\n")
                break
            else:
                print("\nInvalid choice. Try again.\n")


def main():
    login = Login()
    while True:
        print("\nEnter your choice:")
        print("1. Login")
        print("2. Quit\n")
        choice = input()
        if choice == '1':
            username = login.login()
            if not username:
                continue
            elif username == "admin":
                admin = Librarian()
                admin.menu()
            else:
                customer = Person()
                cursor.execute('SELECT person_id FROM persons WHERE username = ?', (username,))
                user_id = cursor.fetchone()
                customer.menu(user_id[0])
        elif choice == '2':
            print("\nGoodbye!\n")
            conn.close()
            break
        else:
            print("\nInvalid choice. Try again.\n")


if __name__ == "__main__":
    main()
