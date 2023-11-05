"""2. Написати функцію <bank> , яка працює за наступною логікою: користувач робить 
вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу 
збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також 
нараховуються відсотки). Параметр <percents> є необов'язковим і має значення
по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку, а також її повернути 
(але округлену до копійок)."""


def bank(start_amount, years, percents=10):
    try:
        start_amount = int(start_amount)
        percents = int(percents)
    except ValueError:
        try:
            start_amount = float(start_amount)
            percents = float(percents)
        except ValueError:
            print("Incorrect input!")
    for i in range(years):
        income = start_amount * percents/100
        start_amount +=  income
    print(f"Your current state of bank account is {start_amount:.2f}")    
    return round(start_amount, 2)


if __name__ == "__main__":

    start_amount = input("Please enter amount of money: ")
    years = input("Please enter quantity of years: ")
    try:
        years = int(years)
    except ValueError:
        print("Incorrect input!")
        exit()
    percents = input("Please enter percents for year: ")
    if percents.strip():   
        bank(start_amount, years, percents)
    else:
        bank(start_amount, years)