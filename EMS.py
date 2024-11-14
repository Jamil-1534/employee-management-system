from customtkinter import *
from PIL import Image

window=CTk()
window.geometry('930x580') 
window.resizable (False, False) 
window.title('Employee Management System')

Logo=CTkImage(Image.open('poster.png'),size=(930,158)) 
logoLabel=CTkLabel(window, image=Logo, text='') 
logoLabel.grid(row=0,column=0,columnspan=2) 

leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

window.mainloop()

"""start after 46 me"""