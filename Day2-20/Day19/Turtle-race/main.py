from turtle import Turtle,Screen
from random import  randint
timmy=Turtle()
tommy=Turtle()
jimmy=Turtle()
johny=Turtle()
jacky=Turtle()
nimmy=Turtle()
sc=Screen()
sc.setup(width=500,height=400)

user_inp=sc.textinput(title="Make your bet",prompt="which turtle will win the race? predict the color : ")
colors=["red","blue","orange","purple","green","yellow"]
y_pos=[-70,-40,-10,20,50,80]
new_tur=[timmy,tommy,jimmy,johny,jacky,nimmy]
for i in range(0,6):
    new_tur[i].shape("turtle")
    new_tur[i].color(colors[i])
    new_tur[i].penup()
    new_tur[i].goto(-240,y_pos[i])

if user_inp:
    race=True
raceover=False
while race:
     for i in new_tur:
         if i.xcor()>228:
             race=False
             win_tur=i.pencolor()
             if user_inp==win_tur:
                 print(f"Your guess is correct! The winning turtle is {win_tur} you won the race")
                 raceover=True
             else:
                 print(f"you lost! The winning turtle is {win_tur}")
         if raceover==True:
             break

         pos=randint(0,10)
         i.forward(pos)


sc.exitonclick()