"""Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку 
(границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.
"""

initial_year = int(input("Please enter initial year (format  - YYYY): "))
final_year = int(input("Please enter final year (format  - YYYY): "))
for year in range(initial_year, final_year+1):
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        print(year) 





