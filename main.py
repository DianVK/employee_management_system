from tkinter import *

root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20)

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0,padx=10,pady=10)
txtName = Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10)

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=1, column=2)
txtAge = Entry(entries_frame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3)

lbldoj = Label(entries_frame, text="D.O.J.", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0)
txtDoj = Entry(entries_frame,textvariable=doj,font=("Calibri",16),width=30)
txtDoj.grid(row=2,column=1)

# Table Frame
root.mainloop()
