from turtle import Screen
from paddle import paddle
from ball import Ball
from scoreboard import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("ping-pong")
screen.tracer(0)
lpad=paddle(350,0)
rpad=paddle(-350,0)
ball=Ball()
score=Score()

screen.listen()
screen.onkey(key="Up", fun=rpad.up)
screen.onkey(key="Down", fun=rpad.down)
screen.onkey(key="w", fun=lpad.up)
screen.onkey(key="s", fun=lpad.down)
score.__init__()
game=True
x=0.1
while game:
    screen.update()
    ball.ball_move()
    time.sleep(x)
    if ball.ycor()> 280 or ball.ycor()<-280:
        ball.ycollide()
    if ball.distance(rpad) < 50 or ball.xcor() > 380 or ball.distance(lpad) < 50 or ball.xcor() < -380:
        ball.xcollide()
        x*=0.9
    if ball.xcor()>378:
        ball.rxcorn()
        x=0.1
        score.ltscore()

    if ball.xcor()<-380:
        ball.lxcorn()
        x=0.1
        score.rtscore()
screen.exitonclick()





