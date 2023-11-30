""" 1. Напишіть програму, де клас «геометричні фігури» (Figure) містить 
властивість color з початковим значенням white і метод для зміни кольору 
фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять 
методи __init__ для завдання початкових розмірів об'єктів при їх створенні."""

class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side


if __name__ == "__main__":
    oval = Oval(10, 12)
    square = Square(10)
    print(f"Start color: {oval.color}")
    print(f"Start color: {square.color}")
    oval.change_color('red')
    square.change_color('blue')
    print(f"Changed oval color: {oval.color}")
    print(f"Changed sqaure color: {square.color}")
