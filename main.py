from turtle import *
import random
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
window=Screen()
window.setup(width=600,height=600)
window.bgcolor("black")
window.listen()
window.tracer(0)
timmy=Snake()
ball=Food()
table=Scoreboard()
window.onkey(timmy.move_forward,"w")
window.onkey(timmy.move_left,"a")
window.onkey(timmy.move_right,"d")
window.onkey(timmy.move_backward,"s")
game_on=True
while game_on :
    window.update()
    sleep(0.1)
    if timmy.header.distance(ball) <15:
        ball.spawn()
        table.inscrease()
        timmy.extend()
    if timmy.header.xcor() >= 280 or timmy.header.ycor() >= 280 or timmy.header.ycor() <= -280 or timmy.header.xcor() <= -280:
        table.reset()
        timmy.reset()
    
    for i in timmy.segments[1:]:
            if timmy.header.distance(i) < 12 :
                table.reset()
                timmy.reset()
                
    timmy.move()
 
 
   









window.mainloop()
