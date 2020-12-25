from turtle import Turtle,Screen
pos = [20, 0, -20]
dis=20
left=180
right=0
top=90
bottom=270
class Snake:
    def __init__(self):
        self.turt = []
        self.snake()
    def snake(self):
        for i in range(0, 3):
            nw_turt = Turtle()
            nw_turt.shape("square")
            nw_turt.color("white")
            nw_turt.penup()
            nw_turt.setpos(pos[i], 0)
            self.turt.append(nw_turt)
    def move(self):
        pos = self.turt[0].pos()
        self.turt[0].forward(dis)
        if self.turt[2].pos() != self.turt[1].pos():
            self.turt[2].goto(self.turt[1].pos())
        if self.turt[1].pos() != pos:
            self.turt[1].goto(pos)
    def left(self):
        if self.turt[0].heading()!=right:
          self.turt[0].setheading(left)
    def right(self):
        if self.turt[0].heading() != left:
          self.turt[0].setheading(right)
    def up(self):
        if self.turt[0].heading() != bottom:
          self.turt[0].setheading(top)
    def down(self):
        if self.turt[0].heading() !=top:
          self.turt[0].setheading(bottom)