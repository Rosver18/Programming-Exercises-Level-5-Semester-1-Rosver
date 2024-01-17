from tkinter import *

def save_data():
    user_data = user_var.get()
    age_data = age_var.get()
    home_data = home_var.get()

    with open("bio.txt", "w") as file:
        file.write(f"{user_data}\n{age_data}\n{home_data}")
    print(f"Username: {user_data}\nAge: {age_data}\nHometown: {home_data}\n")

root = Tk()
root.resizable(False, False)

user_label = Label(root, text="Username").grid(row=0, column=0)
user_var = StringVar()
user_input = Entry(root, textvariable=user_var).grid(row=0, column=1)

age_label = Label(root, text="Age").grid(row=1, column=0)
age_var = IntVar(value="")
age_input = Entry(root, textvariable=age_var).grid(row=1, column=1)

home_label = Label(root, text="Hometown").grid(row=2, column=0)
home_var = StringVar()
home_input = Entry(root, textvariable=home_var).grid(row=2, column=1)

save_btn = Button(root, text="Save Data", command=save_data).grid(row=3, column=1)

root.mainloop()
