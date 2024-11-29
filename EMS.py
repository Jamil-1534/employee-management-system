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

idLabel=CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold')) 
idLabel.grid (row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold')) 
nameLabel.grid (row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold')) 
phoneLabel.grid (row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
phoneEntry.grid(row=2,column=1,)

roleLabel=CTkLabel(leftFrame, text='role', font=('arial', 18, 'bold')) 
roleLabel.grid (row=3,column=0,padx=20,pady=15,sticky='w')

roleEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
roleEntry.grid(row=3,column=1,)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)


window.mainloop()

"""start after 46 me"""