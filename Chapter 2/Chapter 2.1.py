from tkinter import *

root = Tk()
root.title("The welcome window")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg='yellow')

welcome_label = Label(root, text="Welcome!", font=("Arial", 20, "bold"), bg='yellow')
welcome_label.pack(pady=30)

root.mainloop()
