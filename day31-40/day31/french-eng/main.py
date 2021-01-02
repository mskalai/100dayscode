BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas

def flip():
    canvas.itemconfig(img,image=image2)
    canvas.itemconfig(word,text=list[no]["English"],fill="white")
    canvas.itemconfig(title,text="English",fill="white")

window=Tk()
canvas=Canvas(width=1300,height=1000,bg=BACKGROUND_COLOR)
window.title("French-English Translation")
window.configure(width=900,height=690)
timer=window.after(3000,func=flip)

image1=PhotoImage(file="images/card_front.png")
image2=PhotoImage(file="images/card_back.png")
img=canvas.create_image(800,526,image=image1)
title=canvas.create_text(800,450,text="Title",font=("Arial",30,"italic"))
word=canvas.create_text(800,530,text="Trouve",font=("Arial",40,"bold"))
canvas.place(x=-340,y=-230)
try:
   words=pandas.read_csv("data/words_unknown.csv")
except FileNotFoundError:
   original_words=pandas.read_csv("data/french_words.csv")
   list = pandas.DataFrame(original_words).to_dict(orient="records")
else:
   list=pandas.DataFrame(words).to_dict(orient="records")
no=0
def remove_let():
   list.remove(list[no])
   pandas.DataFrame(list).to_csv("data/words_unknown",index=False)

def next():
    global no,timer
    window.after_cancel(timer)
    no=random.randrange(len(list))
    canvas.itemconfig(word,text=list[no]["French"],fill="black")
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(img,image=image1)
    timer=window.after(3000, func=flip)


#btn(tick)
btnimg1=PhotoImage(file="images/right.png")
btn1=Button(image=btnimg1,highlightthickness=0,command=remove_let)
btn1.place(x=160,y=570)

#btn(Wrong)
btnimg2=PhotoImage(file="images/wrong.png")
btn2=Button(image=btnimg2,highlightthickness=0,command=next)
btn2.place(x=600,y=570)

next()





window.mainloop()

