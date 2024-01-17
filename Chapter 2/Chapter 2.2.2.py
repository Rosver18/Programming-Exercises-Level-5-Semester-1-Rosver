from tkinter import *

root = Tk()
root.title("Exercise 2B")
root.geometry("600x400")
root.configure(bg="LightGray")

left_frame = Frame(root, bd=5, relief=SUNKEN)
left_frame.pack(side=LEFT, fill=BOTH, expand=True)

right_frame = Frame(root, bd=5, relief=SUNKEN)
right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

label_properties = {'padx': 30, 'pady': 5, 'relief': SUNKEN}

label_a = Label(left_frame, bg="#22263E", text="A", fg = "white", **label_properties)
label_b = Label(left_frame, bg="White", text="B", **label_properties)
label_a.pack(side=TOP, fill=BOTH, expand=True)
label_b.pack(side=BOTTOM, fill=BOTH, expand=True)

label_c = Label(right_frame, bg="white", text="C", **label_properties)
label_d = Label(right_frame, bg="#22263E", text="D", fg = "white", **label_properties)
label_c.pack(side=TOP, fill=BOTH, expand=True)
label_d.pack(side=BOTTOM, fill=BOTH, expand=True)

root.mainloop()
