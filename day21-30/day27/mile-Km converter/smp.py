from tkinter import *
val=Tk()
val.minsize(width=600,height=600)
val.title("GUI")
val=Label(text="kalai",font=("Arial",18,"normal"))
val.pack()
#entry
def entry():
    word=input.get()
    val.configure(text=word)
input=Entry()
input.focus()
input.pack()
print(input.get())

#button
def btn_do():
    print("Do something")
btn=Button(text="click me",command=entry)
btn.pack(pady=10)

#text
txt=Text(height=5,width=20)
txt.pack()
txt.focus()
print(txt.get("1.0",END))

#slice
def spin():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=10,command=spin)
spinbox.pack()

#scale
def scale_do(value):
    print(value)
scl=Scale(from_=0,to=20,command=scale_do)
scl.pack()

#checkbox
def check_sel():
 print(check_used.get())
check_used=IntVar()
checkbtn=Checkbutton(text="Is on?",variable=check_used,command=check_sel)
# check_used.get()
checkbtn.pack()

mainloop()



