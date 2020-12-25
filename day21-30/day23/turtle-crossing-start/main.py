import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
player.__init__()
screen.update()
screen.onkey(key="Up",fun=player.move)
car=CarManager()
car.car_create()
score=Scoreboard()
score.__init__()
game_is_on = True
x=0.1
while game_is_on:
    time.sleep(x)
    screen.update()
    car.car_create()
    car.move()
    for cars in car.cars:
        if cars.distance(player)<20:
            game_is_on=False
            score.gameover()

    if player.ycor()>250:
        x*=0.09
        car.new_speed()
        score.lvlup()
        player.move()

screen.exitonclick()