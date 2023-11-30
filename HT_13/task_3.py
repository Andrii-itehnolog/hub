"""3. Створіть клас в якому буде атребут який буде 
рахувати кількість створених екземплярів класів."""


class SomeClass:
    counter = 0
    
    def __init__(self):
        SomeClass.counter += 1


if __name__ == "__main__":
    first = SomeClass()
    print(f"Quantity of created inctances {SomeClass.counter}")
    first = SomeClass()
    print(f"Quantity of created inctances {SomeClass.counter}")
    first = SomeClass()
    print(f"Quantity of created inctances {SomeClass.counter}")