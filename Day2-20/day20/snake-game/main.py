from turtle import Turtle,Screen
from snake import Snake
import time

scrn=Screen()
scrn.setup(width=600,height=600)
scrn.bgcolor("black")
scrn.title("My snake game")
scrn.listen()
scrn.tracer(0)
snake=Snake()
scrn.onkey(snake.up,"Up")
scrn.onkey(snake.left,"Left")
scrn.onkey(snake.right,"Right")
scrn.onkey(snake.down,"Down")

race=True
while race:
    scrn.update()
    time.sleep(0.2)
    snake.move()



























scrn.exitonclick()