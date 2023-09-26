from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Sarthak' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome...')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct details..')


window = Tk()

window.geometry('1530x800+0+0')
window.title('Login Page of Student Management System')
window.resizable(False,False)
backgroundImage = ImageTk.PhotoImage(file='bg1.jpg')

bgLabel = Label(window,image=backgroundImage)
bgLabel.place(x=-50,y=-250)

loginFrame = Frame(window,bg='white')
loginFrame.place(x=500,y=150)
logoImage = PhotoImage(file='profile.png')
logoLabel = Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10,padx=20)

usernameImage = PhotoImage(file='user (1).png')
usernameLabel = Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=10)
usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=10)

passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=10)
passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginButton = Button(loginFrame,text='Login',font=('times new roman',15,'bold'),width=15,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                     activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)
window.mainloop()
