import tkinter
from tkinter import *
from tkinter import messagebox
from login import User, validate_user

root = Tk()
root.geometry("300x300")

#declaring string variable
name_var = tkinter.StringVar()
email_var = tkinter.StringVar()
passw_var = tkinter.StringVar()
confirm_pass_var = tkinter.StringVar()

def submit():

    userID = name_var.get()
    email = email_var.get()
    password = passw_var.get()
    confirm_pass = confirm_pass_var.get()
    user = User(userID,email,password)

    email_var.set("")
    passw_var.set("")
   # confirm_pass.set("")

    return validate_user(user, confirm_pass)


name_label = tkinter.Label(root,text="Username", font=('calibre',10, 'bold'))

name_entry = tkinter.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

email_label = tkinter.Label(root,text="email", font=('calibre',10, 'bold'))

email_entry = tkinter.Entry(root, textvariable=email_var, font=('calibre', 10, 'normal'))


passw_label = tkinter.Label(root, text='Password', font=('calibre', 10, 'bold'))


passw_entry = tkinter.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

confirm_passw_label = tkinter.Label(root, text='Confirm Password', font=('calibre', 10, 'bold'))


confirm_passw_entry = tkinter.Entry(root, textvariable=confirm_pass_var, font=('calibre', 10, 'normal'), show='*')


button = tkinter.Button(master=root, text="Sign in", command=submit)


name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=1)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=1)
confirm_passw_label.grid(row=3,column=0)
confirm_passw_entry.grid(row=3,column=1)
button.grid(row=4,column=1)



root.mainloop()