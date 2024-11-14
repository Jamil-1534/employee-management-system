from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=="or passwordEntry.get()==":
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get()=='jamil' and passwordEntry.get()=='1534':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import EMS
    else:
        messagebox.showerror('Error','wrong credentials')

root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('Login page')

image = CTkImage(Image.open('cover.png'), size=(930, 478))

imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#5c42ff',font=('Gougy Old Style',20,'bold'),text_color='dark orange')
headinglabel.place(x=20,y=100)

usernameEntry= CTkEntry(root,placeholder_text='Enter Your Username',width=180) 
usernameEntry.place(x = 50,y = 140)

passwordEntry= CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*') 
passwordEntry.place(x = 50,y = 180)

loginButton=CTkButton(root, text='Login',cursor='hand2',command=login) 
loginButton.place( x = 70,y = 220 )

root.mainloop()
