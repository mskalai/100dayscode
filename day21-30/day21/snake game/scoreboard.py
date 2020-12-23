from turtle import Turtle
Align="center"
Font=("Courier",18,"normal")
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.scor=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.update()
    def update(self):
        self.write(arg=f"Score :{self.scor}",align=Align,font=Font)
    def gameover(self):
        self.goto(0, 0)
        self.write(arg="Game over!",align=Align,font=Font)


    def scoreinc(self):
        self.scor+=1
        self.clear()
        self.update()


