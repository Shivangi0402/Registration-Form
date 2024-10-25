import tkinter
root=tkinter.Tk()

root.title("Registration Form")

name_label = tkinter.Label(root,text="Enter Name")
name_label.pack()
name_textboox = tkinter.Entry(root)
name_textboox.pack()

age_label = tkinter.Label(root,text="Enter your Age")
age_label.pack()
age_textboox = tkinter.Entry(root)
age_textboox.pack()

Phone_Number_label = tkinter.Label(root,text="Enter Phone Number")
Phone_Number_label.pack()
Phone_Number_textboox = tkinter.Entry(root)
Phone_Number_textboox.pack()

email_label = tkinter.Label(root,text="Enter Email")
email_label.pack()
email_textboox = tkinter.Entry(root)
email_textboox.pack()

submit_button = tkinter.Button(root,text="Submit")
submit_button.pack()

root.mainloop()
