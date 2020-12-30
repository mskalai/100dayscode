from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters=randint(0,18)
    nr_symbols=randint(2,4)
    nr_numbers=randint(2,4)
    password_list=[]
    [password_list.append(choice(letters)) for _ in range(1, nr_letters + 1) ]
    [password_list.append(choice(symbols)) for _ in range(1, nr_symbols + 1) ]
    [password_list.append(choice(numbers)) for _ in range(1, nr_numbers + 1) ]
    shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(END,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    if (website=="" or password==""):
        messagebox.showwarning(title="Warning",message="Please fill out all the fields")
    else:
       is_ok=messagebox.askokcancel(title="Website",message="Do you want to save it?")
    if is_ok:
        with open(r"C:\Users\MS Kalai\Downloads\password-manager-start\Data.txt","a+") as file:
            file.write(f"\n{website} | {email} | {password}")
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry2.insert(END,"example@gmail.com")
        entry3.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.configure(padx=20,pady=20)
canvas=Canvas(width=600,height=500)
window.title("Password Manager")
image_logo=PhotoImage(file="logo.png")
canvas.create_image(310,160,image=image_logo)
canvas.pack()

#website
lbl1=Label(text="Website :",fg="black",font=("Arial",14,"normal"))
lbl1.place(x=80,y=300)
#entry
entry1=Entry(width=50)
entry1.place(x=240,y=305)


#Email/Ussername
lbl2=Label(text="Email/Username :",fg="black",font=("Arial",14,"normal"))
lbl2.place(x=80,y=340)

#entry
entry2=Entry(width=43,font=("Arial",10,"normal"))
entry2.place(x=240,y=345)
entry2.insert(END,"example@gmail.com")


#Password
lbl3=Label(text="Password :",fg="black",font=("Arial",14,"normal"))
lbl3.place(x=80,y=380)
#entry
entry3=Entry(width=25)
entry3.place(x=240,y=385)

#Gn_Password
btn1=Button(text="Generate Password",fg="black",command=gen_password)
btn1.place(x=400,y=381)

#btn
btn=Button(text="Add",width=35,command=save)
btn.place(x=250,y=440)




window.mainloop()