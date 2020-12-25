FONT = ("Courier", 18, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l=1
        self.goto(-270,270)
        self.clear()
        # self.lvl()
    def lvl(self):
         self.clear()
         self.write(f"Level:{self.l}",align="left",font=FONT)

    def lvlup(self):
         self.l+=1
         self.lvl()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over!",align="center",font=FONT)
