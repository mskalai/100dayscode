import colorgram
import random
from turtle import Turtle,Screen
from colorgram import colorgram
timmy=Turtle()
sc=Screen()
# col=colorgram.extract("paint.jpg",30)
# rgb=[]
# for i in col:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     rgb.append((r,g,b))
sc.colormode(255)
timmy.speed(20)
col=[(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
timmy.setheading(225)
timmy.up()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)
for i in range(1,11):
    j=1

    while(j<=10):
        timmy.dot(15)
        timmy.color((random.choice(col)))
        timmy.forward(50)
        if(j%10==0):
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)
        j+= 1
sc.exitonclick()