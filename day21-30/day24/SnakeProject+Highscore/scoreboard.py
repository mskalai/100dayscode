from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            hsc=file.read()
        self.highscore=int(hsc)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
        hs=str(self.highscore)
        with open("data.txt","w") as file:
            file.write(hs)

    def hscore(self):
        if self.score >self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
