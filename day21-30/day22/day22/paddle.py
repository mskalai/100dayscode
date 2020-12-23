from turtle import Turtle

class paddle(Turtle):


    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.setpos(x,y)


    def up(self):
        ycor = self.ycor()
        if ycor < 240:
            ycor += 20
            self.setpos(self.xcor(), ycor)


    def down(self):
        ycor = self.ycor()
        if ycor > -240:
            ycor -= 20
            self.setpos(self.xcor(), ycor)





