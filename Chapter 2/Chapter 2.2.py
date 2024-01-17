from tkinter import *

root = Tk()
root.geometry("200x75")
root.title("Exercise 2A")
root.configure(bg="LightGray")

label_properties = {'padx': 45, 'pady': 4, 'relief': SUNKEN}

labels = [
    Label(root, bg="Red", text="A", **label_properties),
    Label(root, bg="Yellow", text="B", **label_properties),
    Label(root, bg="Blue", text="C", **label_properties),
    Label(root, bg="White", text="D", **label_properties)
]

labels[0].pack(side=TOP, fill=X, expand=True)
labels[1].pack(side=BOTTOM, fill=NONE)
labels[2].pack(side=LEFT, expand=True)
labels[3].pack(fill=NONE)

root.mainloop()