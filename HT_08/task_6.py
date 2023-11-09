""" 6. Напишіть функцію,яка прймає рядок з декількох слів і 
повертає довжину найкоротшого слова. Реалізуйте обчислення за допомогою генератора."""

def shortest_length(test_string):
    words = test_string.split()
    length = min(len(word) for word in words)
    return length


if __name__ == "__main__":
    test = 'Computes the object ID value for an object with specified type with the contents of the named file (which ' \
           'can be outside of the work tree), and optionally writes the resulting object into the object database. ' \
           'Reports its object ID to its standard output. When <type> is not specified, it defaults to "blob" '
    result = shortest_length(test)
    print(f"The length of the shortest word is: {result}")
