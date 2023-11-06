""" 3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000, 
и яка вертатиме True, якщо це число просте і False - якщо ні"""

def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
        return True
    return False


if __name__ == "__main__":
    try:
        number = int(input("Please enter integer from range 0...1000: "))
    except ValueError:
        print("Number must be only integer")
        exit()
    if 0 <= number <=1000:
        print(is_prime(number))
    else:
        print("Number must be only in range 0...1000")
    
