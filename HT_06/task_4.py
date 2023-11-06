"""4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець діапазона,
 і вертатиме список простих чисел всередині цього діапазона. Не забудьте про перевірку на валідність
  введених даних та у випадку невідповідності - виведіть повідомлення."""


def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
        return True
    return False


def prime_list(start, finish):
    prime_list = []
    for i in range(start, finish+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list



if __name__ == "__main__":
    try:
        start_number = int(input("Please enter first integer: "))
        finish_number = int(input("Please enter second integer: "))
        print(prime_list(start_number, finish_number))
    except ValueError:
        print("Numbers must be only integer")
        
    

    
