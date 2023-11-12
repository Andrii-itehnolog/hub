""" 1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска 
   програми на екран виводиться в лівій половині - колір автомобільного, 
   а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори. 
   Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в 
   звичайних світлофорах (пішоходам зелений тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green"""


import time


if __name__ == "__main__":
   color_list = {"Red": "Green", "Yellow": "Red", "Green": "Red"}
   while True:
      for first, second  in color_list.items():
         if first == "Yellow":
            for i in range(2):
               print(f"{first:<8} {second:<8}" )
               time.sleep(1)
         else:
            for i in range(4):
               print(f"{first:<8} {second:<8}" )
               time.sleep(1)
    