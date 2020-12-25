import turtle
import pandas
screen=turtle.Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states=pandas.read_csv("50_states.csv")
states_list=states["state"].to_list()
states_count=[]
score=0
length=len(states_count)
while(score!=50):
    answer = screen.textinput(title=f"Guess the States   States : {score}/50  or 'exit'", prompt="         Enter the state..What you know in U.S          ").title()
    if answer=="Exit":
        break
    if answer in states_list:
        pos=states_list.index(answer)
        nw=turtle.Turtle()
        nw.penup()
        nw.hideturtle()
        nw.speed("fastest")
        x=states.x[pos]
        y=states.y[pos]
        nw.goto(x,y)
        nw.write(answer)
        states_count.append(answer)
        score+=1
for state in states_count:
    states_list.remove(state)
states_unknown={"states":states_list}
pandas.DataFrame(states_unknown).to_csv("states_unknown")

