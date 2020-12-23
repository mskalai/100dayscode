from turtle import Screen
from snake import Snake
from food import food
from scoreboard import score
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

food=food()
score=score()
race=True
while race:
    scrn.update()
    time.sleep(0.2)
    snake.move()

    if snake.turt[0].distance(food)<15:
        food.pos()
        score.scoreinc()
        snake.extend()

    if snake.turt[0].xcor()>280 or snake.turt[0].ycor()>280 or snake.turt[0].xcor()<-280 or snake.turt[0].ycor()<-280:
        score.gameover()
        race=False

    for turtl in snake.turt[1:]:
      if snake.turt[0].distance(turtl)<10:
            score.gameover()
            race=False

scrn.exitonclick()