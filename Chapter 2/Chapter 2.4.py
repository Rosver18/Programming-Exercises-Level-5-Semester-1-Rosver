from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.resizable(False, False)
root.configure(bg="white")


bgcolor = "#E5E5E5" 
fontfill = "#232531" 
entrycolor = "#AEAEB8" 
labelfont = ("Courier New", 12, "bold") 

img = Image.open("logo.png")
resized_img = img.resize((400, 125))
logo = ImageTk.PhotoImage(resized_img)

header = Label(root, image=logo)
header.pack(pady=10)

frame1 = Frame(root, bg=bgcolor)
frame1.pack(padx=5)

title = Label(frame1, text="Student Management System", font=("Arial", 20, "bold"), bg=bgcolor, fg=fontfill)
title.pack()

details = Label(frame1, text="New Student Registration", font=("Arial Black", 12, "bold"), bg=bgcolor, fg=fontfill)
details.pack()

name = Label(frame1, text="Student Name", font=labelfont, bg=bgcolor, fg=fontfill, pady=10, padx=25)
name.pack(side="left")

nameval = StringVar()

name_e = Entry(frame1, textvariable=nameval, width=30, bg=entrycolor, bd=0)
name_e.pack(side="right", padx=20, ipady=5.5)

frame2 = Frame(root, bg=bgcolor)
frame2.pack()

phone = Label(frame2, text="Phone Number", font=labelfont, bg=bgcolor, fg=fontfill, padx=25)
phone.pack(side="left")

phoneval = IntVar(value="") 

phone_e = Entry(frame2, textvariable=phoneval, width=30, bg=entrycolor, bd=0)
phone_e.pack(side="right", padx=20, ipady=5.5)

frame3 = Frame(root, bg=bgcolor)
frame3.pack()

email = Label(frame3, text="E-mail ID", font=labelfont, bg=bgcolor, fg=fontfill, padx=40, pady=10)
email.pack(side="left")

emailval = StringVar()

email_e = Entry(frame3, textvariable=emailval, width=30, bg=entrycolor, bd=0)
email_e.pack(side="right", padx=20, ipady=5.5)

frame4 = Frame(root, bg=bgcolor)
frame4.pack()

address = Label(frame4, text="Address", font=labelfont, bg=bgcolor, fg=fontfill, padx=50, pady=5)
address.pack(side="left")

addressval = StringVar()

address_e = Entry(frame4, textvariable=addressval, width=30, bg=entrycolor, bd=0)
address_e.pack(side="right", padx=20, ipady=5.5)

frame5 = Frame(root, bg=bgcolor)
frame5.pack()

gender = Label(frame5, text="Gender", font=labelfont, bg=bgcolor,fg=fontfill, padx=50, pady=15)
gender.pack(side="left")

genderval = StringVar()

open_icon = Image.open("dropdown triangle.png")
icon = ImageTk.PhotoImage(open_icon.resize((25,25)))

options = ["Male", "Female", "Prefer not to say"] 
gendermenu = OptionMenu(frame5, genderval, *options)
gendermenu.config(
    padx= 50,
    bg=entrycolor, 
    highlightthickness=0, 
    border=0,
    width=12,
    indicatoron= 0,
    )

arrow_label = Label(gendermenu, bd = 0, highlightthickness=0, image=icon, bg=entrycolor) 
arrow_label.place(relx=0.80, rely=0.20) 

def on_enter(event): 
    arrow_label.config(
        bg="#F0F0F0"
    )

def on_leave(event): 
    arrow_label.config(
        bg=entrycolor
    )

gendermenu.bind('<Enter>', on_enter) 
gendermenu.bind('<Leave>', on_leave) 

gendermenu.pack(side="right", padx=30, ipady=5.5)

frame6 = Frame(root, bg=bgcolor)
frame6.pack()

course = Label(frame6, text="Course Enrolled", font=labelfont, bg=bgcolor, fg=fontfill, padx=47, pady=10)
course.grid(row=0, column=0)

courseval = StringVar()
courseval.set("")

choice1 = Radiobutton(frame6, text="BSc CC", variable=courseval, value="BSc CC", font=labelfont, bg=bgcolor, fg=fontfill, padx=25)
choice1.grid(row=0, column=1, sticky="w")

choice2 = Radiobutton(frame6, text="BSc CY", variable=courseval, value="BSc CY", font=labelfont, bg=bgcolor, fg=fontfill, padx=25)
choice2.grid(row=1, column=1, sticky="w")

choice3 = Radiobutton(frame6, text="BSc Psy", variable=courseval, value="BSc Psy", font=labelfont, bg=bgcolor, fg=fontfill, padx=25)
choice3.grid(row=2, column=1, sticky="w")

choice4 = Radiobutton(frame6, text="BA & BM", variable=courseval, value="BA & BM", font=labelfont, bg=bgcolor, fg=fontfill, padx=25)
choice4.grid(row=3, column=1, sticky="w")

frame7 = Frame(root, bg=bgcolor)
frame7.pack()

language = Label(frame7, text="Languages known", font=labelfont, bg=bgcolor, fg=fontfill, padx=5)
language.grid(row=0, column=0)

langvalue = IntVar()

lang1 = Checkbutton(frame7, text="Tagalog", variable=langvalue, font=labelfont, bg=bgcolor, fg=fontfill, offvalue="", onvalue="Tagalog")
lang1.grid(row=0, column=2)

lang2 = Checkbutton(frame7, text="English", variable=langvalue, font=labelfont, bg=bgcolor, fg=fontfill, offvalue="", onvalue="English")
lang2.grid(row=0, column=1)

lang3 = Checkbutton(frame7, text="Hindi/Urdu", variable=langvalue, font=labelfont, bg=bgcolor, fg=fontfill, offvalue="", onvalue="Hindi/Urdu")
lang3.grid(row=1, column=1)

frame8 = Frame(root, bg=bgcolor)
frame8.pack()

comms = Label(frame8, text="Rate your English communication skills", font=labelfont, bg=bgcolor, padx=6, pady=5)
comms.pack()

comms_scale = Scale(frame8, from_=0, to=100, orient="horizontal", bg=bgcolor, highlightthickness=0)
comms_scale.pack()

frame9 = Frame(root, bg=bgcolor)
frame9.pack()

submit = Button(frame9, text="Submit", padx=40, pady=5, bd=0, bg=fontfill, fg="white", font=labelfont)
submit.pack(side="left", padx=27)

clear = Button(frame9, text="Clear", padx=40, pady=5, bd=0, bg=fontfill, fg="white", font=labelfont)
clear.pack(side="right", padx=27, pady=10)

root.mainloop()