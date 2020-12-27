from tkinter import *

window=Tk()
window.minsize(width=400,height=100)
window.title("Mile-Kilometer converter")
def calculate():
   val1 = float(input.get())
   res=round(val1*1.609)
   lab3.configure(text=res)
   lab3.place(x=190,y=80)


#entry
input=Entry()
input.place(x=140,y=40)
input.focus()
input.insert(END,0)



#label1
lab1=Label(text="is equal to",font=("Arial",12))
lab1.place(x=60,y=80)

#label2
lab2=Label(text="Miles",font=("Arial",12))
lab2.place(x=280,y=40)

#label3(o/p)
lab3=Label(text=0,font=(10))
lab3.place(x=190,y=80)

#label4
lab4=Label(text="Km",font=("Arial",12))
lab4.place(x=285,y=80)

#button
btn=Button(text="Calculate",width=15,command=calculate)
btn.place(x=145,y=120)



window.mainloop()