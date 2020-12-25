COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import  Turtle
import random
class CarManager:
    def __init__(self):
        self.cars=[]
        self.car_speed=MOVE_INCREMENT
    def car_create(self):
            car_chance=random.randrange(1,6)
            if car_chance==5:
                nw_car=Turtle()
                nw_car.shape("square")
                nw_car.setheading(180)
                nw_car.shapesize(stretch_wid=1, stretch_len=2)
                nw_car.penup()
                nw_car.color(random.choice(COLORS))
                nw_car.setpos(290, random.randrange(-240,240))
                nw_car.speed(self.car_speed)
                self.cars.append(nw_car)

    def move(self):
         for car in self.cars:
             car.forward(STARTING_MOVE_DISTANCE)

    def new_speed(self):
         self.car_speed+=MOVE_INCREMENT




