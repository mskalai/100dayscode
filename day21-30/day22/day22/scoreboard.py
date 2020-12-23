from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore =0
        self.rscore =0
        self.setpos(-100, 265)
 
    def ltscore(self):

        self.lscore+=1
        self.update_s()

    def rtscore(self):

        self.rscore += 1
        self.update_s()
    def update_s(self):
        self.clear()
        self.setpos(-100, 265)
        self.write(f"Score :{self.lscore}",align="center",font=("Courier",24,"normal"))
        self.setpos(100, 265)
        self.write(f"Score :{self.rscore}",align="center", font=("Courier", 24, "normal"))




