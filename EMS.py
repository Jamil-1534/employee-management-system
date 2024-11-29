from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(), roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','Data is updated')


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])


def clear():
    idEntry.delete(0, END)           
    nameEntry.delete(0, END)         
    phoneEntry.delete(0, END)                  
    salaryEntry.delete(0, END)      
 
#-----------------------
def treeview_data():
    for item in tree.get_children():
        tree.delete(item)
        
    employees = database.fetch_employees()  
    for employee in employees:
    
        tree.insert('', 'end', values=employee)
#--------2.11.23-------------------------

def add_employee(): 
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fiends are required')
    
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')


window=CTk()
window.geometry('930x580+100+100') 
window.resizable (False, False) 
window.title('Employee Management System')
window.configure(fg_color='#161030')

Logo=CTkImage(Image.open('poster.png'),size=(930,158)) 
logoLabel=CTkLabel(window, image=Logo, text='') 
logoLabel.grid(row=0,column=0,columnspan=2) 

leftFrame=CTkFrame(window,fg_color='#161030')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'),text_color='white') 
idLabel.grid (row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'),text_color='white') 
nameLabel.grid (row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'),text_color='white') 
phoneLabel.grid (row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
phoneEntry.grid(row=2,column=1,)

roleLabel=CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'),text_color='white') 
roleLabel.grid (row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer', 
              'DevOps Engineer', 'Data Scientist', 'Business Analyst', 'IT Consultant', 'UX/UI Designer']
roleBox=CTkComboBox (leftFrame, values=role_options, width=180, font=('arial', 15, 'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set('Search By') 

genderLabel=CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'),text_color='white') 
genderLabel.grid (row=4,column=0,padx=20,pady=15,sticky='w')

gender_option=['Male', 'Female']
genderBox=CTkComboBox (leftFrame, values=gender_option, width=180, font=('arial', 15, 'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set('Search By') 

salaryLabel=CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'),text_color='white') 
salaryLabel.grid (row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=188) 
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)


search_options=['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary'] 
searchBox=CTkComboBox(rightFrame, values=search_options, state= 'readonly')
searchBox.grid(row=0,column=0) 
searchBox.set('Search By') 
searchEntry=CTkEntry(rightFrame) 
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame, text='Search', width=100) 
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame, text='Show All', width=100) 
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary') 

tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=140)


style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview', font=('arial', 12, 'bold'),rowheight=25, background='#000000', foreground='white')

scrollbar=ttk.Scrollbar (rightFrame, orient=VERTICAL,) 
scrollbar.grid(row=1,column=4,sticky='ns')

buttonFrame=CTkFrame(window,fg_color='#161030')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15)
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160,corner_radius=15)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame, text='Delete All',font=('arial', 15, 'bold'), width=160,corner_radius=15)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

window.bind('<ButtonRelease>', selection)

window.mainloop()


"""start after 2.38.42 me"""