""" 2. Створити клас Person, в якому буде присутнім метод __init__ який буде 
приймати якісь аргументи, які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут 
profession (його не має інсувати під час ініціалізації)."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(f"{self.name}'s age is {self.age}.")

    def print_name(self):
        print(f"Name: {self.name}")

    def show_all_information(self):
        print(f"Name: {self.name}, Age: {self.age}")


person1 = Person(name="Andrii", age=20)
person2 = Person(name="Oleg", age=35)

person1.profession = "Engineer"
person2.profession = "Doctor"

person1.print_name()
person1.show_age()
person1.show_all_information()
print(f"Profession: {person1.profession}")

person2.print_name()
person2.show_age()
person2.show_all_information()
print(f"Profession: {person2.profession}")

