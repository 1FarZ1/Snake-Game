from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.goto(x=random.randint(-270,270),y=random.randint(-270,270))
    def spawn(self):
        new_x=random.randint(-270,270)
        new_y=random.randint(-270,270)
        self.goto(new_x,new_y)