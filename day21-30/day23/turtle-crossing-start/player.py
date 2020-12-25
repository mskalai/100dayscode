STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280
from turtle import Turtle
class Player(Turtle):
     def __init__(self):
         super().__init__()
         self.shape("turtle")
         self.setheading(90)
         self.penup()
         self.setpos(STARTING_POSITION)
     def move(self):
          if self.ycor()<250:
              self.forward(MOVE_DISTANCE)
          else:
              self.goto(STARTING_POSITION)


