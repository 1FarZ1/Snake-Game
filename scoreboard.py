from turtle import Turtle
import random
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.score=0
        with open("Day20/data.text") as file:  
            self.high_score=int(file.read())
        self.goto(x=0,y=250)
        self.write_f()
    
    def inscrease(self):
        self.clear()
        self.score+=1
        self.write_f()
    def write_f(self):
        self.write(f"Score : {self.score} High score : {self.high_score}", align='center', font=('Arial', 20, 'normal'))
    def reset(self):
        if self.score > self.high_score:
            with open("Day20/data.text","w") as file:  
                file.write(f"{self.score}")
            self.high_score=self.score
        self.score=0
        self.clear()
        self.write_f()
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over", align='center',font=('Arial', 30,"normal"))