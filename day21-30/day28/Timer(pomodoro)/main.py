from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

window=Tk()


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window.title("Podomaro")
window.configure(padx=100,pady=80,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
time=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.pack()

#label(timer)

lbl1=Label(text="Timer",font=(FONT_NAME,24,"normal"),fg=GREEN,highlightthickness=0,bg=YELLOW)
lbl1.place(x=55,y=-50)
def reset_timer():
    global  reps
    window.after_cancel(timer)
    canvas.itemconfig(time,text="00:00")
    lbl1.configure(text="Timer")
    lbl2.configure(text="")
    reps=0

def count_down(count):
   count_min=math.floor(count/60)
   count_sec=count%60
   if count_sec<10:
       count_sec=f"0{count_sec}"
   canvas.itemconfig(time,text=f"{count_min}:{count_sec}")
   if count>0:
    global timer
    timer=window.after(1000,count_down,count-1)
   else:
       timer_c()
       marks=''
       for i in range(math.floor(reps/2)):
           marks+='✔'
       lbl2.configure(text='✔')
def timer_c():
    global reps
    reps+=1
    work_sec=0
    if reps==1 or reps==3 or reps==5 or reps==7:
        work_sec=WORK_MIN*60
        lbl1.configure(text="Work",fg=GREEN)
    elif reps ==2 or reps==4 or reps==6:
        work_sec=SHORT_BREAK_MIN*60
        lbl1.configure(text="Break",fg=PINK)
    elif reps==8:
        work_sec = LONG_BREAK_MIN * 60
        lbl1.configure(text="Break", fg=RED)
    count_down(work_sec)

#btn
btn1=Button(text="Start",highlightthickness=0,command=timer_c)
btn1.place(x=-30,y=250)
#btn2
btn2=Button(text="Reset",highlightthickness=0,command=reset_timer)
btn2.place(x=170,y=250)

#label
lbl2=Label(text="")
lbl2.place(x=90,y=240)





window.mainloop()