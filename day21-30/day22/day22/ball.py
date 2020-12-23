from turtle import  Turtle
import random
class Ball(Turtle):
     def __init__(self):
         super().__init__()

         self.xmov=10
         self.ymov=10
         self.shape("circle")
         self.color("blue")
         self.setpos(0,0)
         self.penup()

     def ball_move(self):
         newx=self.xcor()+self.xmov
         newy=self.ycor()+self.ymov
         self.setpos(newx,newy)

     def ycollide(self):
         self.ymov*=-1

     def xcollide(self):
         self.xmov*=-1

     def rxcorn(self):
         self.setpos(0,0)
         self.xcollide()

     def lxcorn(self):
         self.setpos(0,0)
         self.ycollide()
        


