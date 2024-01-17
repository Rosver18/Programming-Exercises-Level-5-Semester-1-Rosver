from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def update_order():
    coffee = coffee_var.get()
    size = size_var.get()
    milk = milk_var.get()
    messagebox.showinfo('Order', f"You have received a {size} {coffee} with {milk} milk.")

root = Tk()
root.title("Coffee Club Vending Machine")
root.resizable(False, False)
root.configure(bg="#CDBBAC")

frame = Frame(root, bg="#CDBBAC")
frame.pack(padx=10)

title = Label(frame, text="Coffee Club", fg="black", font=("Arial Black", 25, "bold"), bg="#CDBBAC")
title.pack(padx=10)

coffee_var = StringVar()
coffee_label = Label(frame, text="| COFFEE DRINKS |", fg="black", font=("Arial Black", 12, "bold"), padx=10, pady=10, bg="#CDBBAC")
coffee_label.pack(padx=10, pady=10)

img1 = Image.open("espresso.png")
espresso_img = ImageTk.PhotoImage(img1.resize((100, 100)))

espresso_label = Label(frame, image=espresso_img, bg="#CDBBAC")
espresso_label.pack(side="left", padx=24)

espresso_btn = Radiobutton(frame, text="Espresso", fg="black", font=("Arial Black", 10, "bold"), variable=coffee_var, value="espresso", bg="#CDBBAC")
espresso_btn.pack(side="left")

img2 = Image.open("Americano.png")
americano_img = ImageTk.PhotoImage(img2.resize((100, 100)))

americano_label = Label(frame, image=americano_img, bg="#CDBBAC")
americano_label.pack(side="left", padx=10)

americano_btn = Radiobutton(frame, text="Americano", fg="black", font=("Arial Black", 10, "bold"), variable=coffee_var, value="americano", padx=10, bg="#CDBBAC")
americano_btn.pack(side="left")

frame2 = Frame(root, bg="#CDBBAC")
frame2.pack(padx=10)

img3 = Image.open("Risretto.png")
retto_img = ImageTk.PhotoImage(img3.resize((100, 100)))

retto_label = Label(frame2, image=retto_img, bg="#CDBBAC")
retto_label.pack(side="left", padx=10)

retto_btn = Radiobutton(frame2, text="Risretto", fg="black", font=("Arial Black", 10, "bold"), variable=coffee_var, value="risretto", bg="#CDBBAC")
retto_btn.pack(side="left", padx=24)

img4 = Image.open("mocha.png")
mocha_img = ImageTk.PhotoImage(img4.resize((100, 100)))

mocha_label = Label(frame2, image=mocha_img, bg="#CDBBAC")
mocha_label.pack(side="left")

mocha_btn = Radiobutton(frame2, text="Mocha", fg="black", font=("Arial Black", 10, "bold"), variable=coffee_var, value="mocha", bg="#CDBBAC")
mocha_btn.pack(side="left", padx=20)

frame3 = Frame(root, bg="#CDBBAC")
frame3.pack()

size_var = StringVar()

size_label = Label(frame3, text="| SIZE |", fg="black", font=("Arial Black", 12, "bold"), padx=10, pady=10, bg="#CDBBAC")
size_label.pack(padx=142, pady=20)

small_btn = Radiobutton(frame3, text="Small", fg="black", font=("Arial Black", 13, "bold"), variable=size_var, value="small", bg="#CDBBAC")
small_btn.pack(side="left", padx=60)

medium_btn = Radiobutton(frame3, text="Medium", fg="black", font=("Arial Black", 13, "bold"), variable=size_var, value="medium", bg="#CDBBAC")
medium_btn.pack(side="left", padx=30)

large_btn = Radiobutton(frame3, text="Large", fg="black", font=("Arial Black", 13, "bold"), variable=size_var, value="large", bg="#CDBBAC")
large_btn.pack(side="left", padx=60)

frame4 = Frame(root, bg="#CDBBAC")
frame4.pack()

milk_var = StringVar()

milk_label = Label(frame4, text="| MILK |", fg="black", font=("Arial Black", 12, "bold"), padx=10, pady=10, bg="#CDBBAC")
milk_label.pack(padx=20, pady=20)

fresh_btn = Radiobutton(frame4, text="Fresh", fg="black", font=("Arial Black", 10, "bold"), variable=milk_var, value="fresh", bg="#CDBBAC")
fresh_btn.pack(side="left", padx=20)

soy_btn = Radiobutton(frame4, text="Soy", fg="black", font=("Arial Black", 10, "bold"), variable=milk_var, value="soy", bg="#CDBBAC")
soy_btn.pack(side="left", padx=12)

coco_btn = Radiobutton(frame4, text="Coconut", fg="black", font=("Arial Black", 10, "bold"), variable=milk_var, value="coconut", bg="#CDBBAC")
coco_btn.pack(side="left", padx=12)

protein_btn = Radiobutton(frame4, text="Protein", fg="black", font=("Arial Black", 10, "bold"), variable=milk_var, value="protein", bg="#CDBBAC")
protein_btn.pack(side="left", padx=20)

frame5 = Frame(root, bg="#CDBBAC")
frame5.pack()

order_btn = Button(frame5, text="ORDER", bg="#AA9C92", fg="black", font=("Arial Black", 12, "bold"), padx=10, pady=5, bd=0, command=update_order)
order_btn.pack(padx=169, pady=10)

order_text = Label(frame5, text="", font=("Arial Black", 10), bg="#CDBBAC")
order_text.pack(pady=10)

root.mainloop()
