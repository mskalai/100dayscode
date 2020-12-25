from turtle import Turtle,Screen
timmy=Turtle()
sc=Screen()
def move():
    timmy.forward(10)
def back():
    timmy.backward(10)
def cclock():
    timmy.right(-10)

def clock():
    timmy.right(10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()()


sc.listen()
sc.onkey(key="w",fun=move)
sc.onkey(key="s", fun=back)
sc.onkey(key="a",fun=cclock)
sc.onkey(key="d", fun=clock)
sc.onkey(key="c",fun=clear)
sc.exitonclick()
