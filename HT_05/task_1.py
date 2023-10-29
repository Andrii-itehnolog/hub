""" 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення - виводити відповідне повідомлення."""


def get_season(number_of_month):
    season_dict = {
        "winter": (12, 1, 2),
        "spring": (3, 4, 5),
        "summer": (6, 7, 8),
        "autumn": (9, 10, 11)
    }
    if number_of_month in range(1, 13):
        for key, value in season_dict.items():
            if number_of_month in value:
                return key
    else:
        return "Wrong input! Value must be only number between 1 and 12!"


if __name__ == "__main__":
    user_input = input("Please, enter number of month(1-12): ")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Error! Value must be only number between 1 and 12!")
    else:
        print(f"The month number {user_input} is {get_season(user_input)}")
