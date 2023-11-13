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
   color_list = ["Red", "Yellow", "Green", "Yellow"]
   color_dict = {"Red": "Green", "Yellow": "Red", "Green": "Red"}
   while True:
      for item  in color_list:
         if item == "Yellow":
            for i in range(2):
               print(f"{item:<8} {color_dict[item]:<8}" )
               time.sleep(1)
         else:
            for i in range(4):
               print(f"{item:<8} {color_dict[item]:<8}" )
               time.sleep(1)
    