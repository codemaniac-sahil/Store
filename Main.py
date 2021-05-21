from tkinter import *
from Admin import admin
from User import user
root=Tk()
root.title('Reliance Store')
f1=Frame(root,bg='#0398fc',height=200)
Label(f1,text='Reliance store\n',bg='#0398fc',font='corbel 18 bold').pack()
f1.pack(fill='x',pady=15,padx=23)
Label(root,text='Welcome to reliance store ,here you can get everything online',font='corbel 10 ').place(x=300,y=200)

def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='' and S2==''):
        admin()
    elif(S1=='root' and S2=='pass'):
        admin() 
    else:
        error=Label(root,text="Wrong Id \n Password \n TRY AGAIN",fg="red",font="helvetica 12 bold")
        error.place(x=650,y=400)

username=Label(root,text="USERNAME",font='corbel 12 bold')
userbox = Entry(root)
password=Label(root,text="PASSWORD",font='corbel 12 bold')
passbox = Entry(root,show="*")
login = Button(root, text="LOGIN", command=GET,font="arial 8 bold")
Label(root,text='If you are not admin ').place(x=510,y=450)
not_admin=Button(root,text='Go to store',command=user)
not_admin.place(x=510,y=500)
username.place(x=450,y=270)
userbox.place(x=650,y=270)
password.place(x=450,y=310)
passbox.place(x=650,y=310)
login.place(y=350,x=610)
    



root.mainloop()
