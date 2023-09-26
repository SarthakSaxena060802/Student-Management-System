from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas

# functionality part...

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['Roll No.','Name','Department','Year','Gender','Mobile No.','Email','D.O.B','Address','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success', 'Data is saved successfully..')

def update_student():

    def update_data():
        date = time.strftime('%d/%m/%Y')
        currtime = time.strftime('%H/%M/%S')

        query=('update student set Name=%s, Department=%s, Year=%s, Gender=%s, Mobile=%s, Email=%s, Dob=%s, '
               'Address=%s, AddedDate=%s, AddedTime=%s where Rollno=%s')
        mycursor.execute(query,(nameEntry.get(), departmentEntry.get(), yearEntry.get(), genderEntry.get(),
                                mobileEntry.get(), emailEntry.get(), dobEntry.get(), addressEntry.get(), date, currtime, idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Roll No. {idEntry.get()} is modified successfully..', parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.grab_set()
    update_window.title('Update Student..')
    update_window.geometry('500x680+450+50')
    update_window.resizable(False, False)

    idLabel = Label(update_window, text='Roll No.', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    departmentLabel = Label(update_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, pady=15, padx=10)

    yearLabel = Label(update_window, text='Year', font=('times new roman', 20, 'bold'))
    yearLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    yearEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    yearEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=4, column=1, pady=15, padx=10)

    mobileLabel = Label(update_window, text='Mobile No.', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=5, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=6, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=8, column=1, pady=15, padx=10)

    update_button = ttk.Button(update_window, text='UPDATE', command=update_data)
    update_button.grid(row=10, columnspan=2, pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']

    idEntry.insert(0,listdata[0])
    nameEntry.insert(1,listdata[1])
    departmentEntry.insert(2,listdata[2])
    yearEntry.insert(3,listdata[3])
    genderEntry.insert(4,listdata[4])
    mobileEntry.insert(5,listdata[5])
    emailEntry.insert(6,listdata[6])
    dobEntry.insert(7,listdata[7])
    addressEntry.insert(8,listdata[8])

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where Rollno=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Roll No. {content_id} deleted successfully..')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def search_student():
    def search_data():
        query = ('select * from student where Rollno=%s or Name=%s or Department=%s or '
                 'Year=%s or Gender=%s or Mobile=%s or Email=%s or Dob=%s or Address=%s')
        mycursor.execute(query,
                         (idEntry.get(), nameEntry.get(), departmentEntry.get(), yearEntry.get(), genderEntry.get(),
                          mobileEntry.get(), emailEntry.get(), dobEntry.get(), addressEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.grab_set()
    search_window.title('Search Student..')
    search_window.geometry('500x680+450+50')
    search_window.resizable(False, False)

    idLabel = Label(search_window, text='Roll No.', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    departmentLabel = Label(search_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, pady=15, padx=10)

    yearLabel = Label(search_window, text='Year', font=('times new roman', 20, 'bold'))
    yearLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    yearEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    yearEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=4, column=1, pady=15, padx=10)

    mobileLabel = Label(search_window, text='Mobile No.', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=5, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=6, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=8, column=1, pady=15, padx=10)

    search_button = ttk.Button(search_window, text='SEARCH', command=search_data)
    search_button.grid(row=10, columnspan=2, pady=15)

def add_student():
    def add_data():
        date = time.strftime('%d/%m/%Y')
        currtime = time.strftime('%H/%M/%S')
        if idEntry.get() == '' or nameEntry.get() == '' or departmentEntry.get() == '' or yearEntry.get() == '' or genderEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or dobEntry.get() == '' or addressEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=add_window)

        else:

            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                    idEntry.get(), nameEntry.get(), departmentEntry.get(), yearEntry.get(), genderEntry.get(),
                    mobileEntry.get(), emailEntry.get(), dobEntry.get(), addressEntry.get(), date, currtime))
                con.commit()
                result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to add another?',
                                             parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    departmentEntry.delete(0, END)
                    yearEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    dobEntry.delete(0, END)
                    addressEntry.delete(0, END)
                else:
                    add_window.destroy()
            except:
                messagebox.showerror('Error', 'Roll No. cannot be repeated', parent=add_window)
                return

            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('', END, values=data)

    add_window = Toplevel()
    add_window.grab_set()
    add_window.title('Add Student..')
    add_window.geometry('500x680+450+50')
    add_window.resizable(False, False)

    idLabel = Label(add_window, text='Roll No.', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    departmentLabel = Label(add_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, pady=15, padx=10)

    yearLabel = Label(add_window, text='Year', font=('times new roman', 20, 'bold'))
    yearLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    yearEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    yearEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=4, column=1, pady=15, padx=10)

    mobileLabel = Label(add_window, text='Mobile No.', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=5, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=6, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=7, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=8, column=1, pady=15, padx=10)

    add_student_button = ttk.Button(add_window, text='ADD STUDENT', command=add_data)
    add_student_button.grid(row=10, columnspan=2, pady=15)

def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())  # connectiong with the database
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(Rollno varchar(50) not null primary key, Name varchar(30), Department varchar(30), Year varchar(10), Gender varchar(10), Mobile varchar(15), Email varchar(40), Dob varchar(20), Address varchar(50), AddedDate varchar(30), AddedTime varchar(30))'
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)
    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)


count = 0
text = ''
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(100, slider)

def clock():
    date = time.strftime('%d/%m/%Y')
    currtime = time.strftime('%H/%M/%S')
    datetimeLabel.config(text=f'    Date: {date}\nTime: {currtime}')
    datetimeLabel.after(1000, clock)

# gui part...

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1530x800+0+0')
root.title('Student Management System')
root.resizable(False, False)

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=35)
clock()
s = 'Student Management System'
sliderLabel = Label(root, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=400, y=20)
slider()

connectButton = ttk.Button(root, text='Connect to Database', command=connect_database)
connectButton.place(x=1300, y=35)

leftFrame = Frame(root, bg='white', padx=75, pady=50)
leftFrame.place(x=20, y=100, width=400, height=680)

logo_image = PhotoImage(file='student.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0, pady=10)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, pady=15)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=search_student)
searchstudentButton.grid(row=2, column=0, pady=15)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=15)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED, command=update_student)
updatestudentButton.grid(row=4, column=0, pady=15)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED, command=show_student)
showstudentButton.grid(row=5, column=0, pady=15)

exportButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, command=export_data)
exportButton.grid(row=6, column=0, pady=15)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=7, column=0, pady=15)

rightFrame = Frame(root, bg='white', padx=5, pady=50)
rightFrame.place(x=450, y=100, width=1050, height=680)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=(
    'Roll No.', 'Name', 'Department', 'Year', 'Gender', 'Mobile No.', 'Email', 'D.O.B', 'Address', 'Added Date',
    'Added Time'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)
studentTable.heading('Roll No.', text='Roll No.')
studentTable.heading('Name', text='Name')
studentTable.heading('Department', text='Department')
studentTable.heading('Year', text='Year')
studentTable.heading('Gender', text='Gender')
studentTable.heading('Mobile No.', text='Mobile No.')
studentTable.heading('Email', text='Email')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Address', text='Address')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.column('Roll No.', width=100, anchor=CENTER)
studentTable.column('Name', width=250, anchor=CENTER)
studentTable.column('Department', width=150, anchor=CENTER)
studentTable.column('Year', width=100, anchor=CENTER)
studentTable.column('Gender', width=100, anchor=CENTER)
studentTable.column('Mobile No.', width=180, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('D.O.B', width=150, anchor=CENTER)
studentTable.column('Address', width=300, anchor=CENTER)
studentTable.column('Added Date', width=150, anchor=CENTER)
studentTable.column('Added Time', width=150, anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=30, font=('arial',12,'bold'))
style.configure('Treeview.Heading',font=('arial',13,'bold'),foreground='black')

studentTable.config(show='headings')

root.mainloop()
