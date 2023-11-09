""" 4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну 
послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення 
з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - 
ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   ....... """


def generator(sequence):
    length = len(sequence)
    index = 0
    while True:
        yield sequence[index]
        index = (index + 1) % length


if __name__ == "__main__":
    # test = [1, 2, 3]
    # test = "Geekhub"
    test = (1, 2, 3)
    
    
    for elem in generator(test):
        print(elem)

  
