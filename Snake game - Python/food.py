from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.penup()
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_pos = random.randint(-280, 280)
        self.goto(random_pos, random_pos)
