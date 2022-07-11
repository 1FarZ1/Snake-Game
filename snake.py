from turtle import Turtle
import random
from time import sleep
cord=[(0,0),(-20,0),(-40,0)]
snake=[]



class Snake(Turtle):
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.header=self.segments[0]
      
        
    def create_snake(self):
        for i in cord:
            self.add_segment(i)
    def add_segment(self,position):
        tim=Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1): 
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.header.forward(20)
    def move_forward(self):
        if self.header.heading() != 270 :
            self.header.setheading(90)
    def move_backward(self):
        if self.header.heading() != 90 :
            self.header.setheading(270)
    def move_left(self):
        if self.header.heading() != 0 :
            self.header.setheading(180)
    def move_right(self):
        if self.header.heading() != 180 :
            self.header.setheading(0)
    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.header=self.segments[0]