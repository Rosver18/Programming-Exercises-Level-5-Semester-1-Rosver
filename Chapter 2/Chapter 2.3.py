from tkinter import *


root = Tk()
root.title("Login Page")
root.geometry("400x300") 

Label(root, text="Username:", font=('Arial', 14)).grid(row=0, column=0, sticky=E, pady=10)
Label(root, text="Password:", font=('Arial', 14)).grid(row=1, column=0, sticky=E, pady=10)

entry_username = Entry(root, font=('Arial', 14))
entry_password = Entry(root, show="*", font=('Arial', 14))

entry_username.grid(row=0, column=1, pady=10, padx=(0, 10))  
entry_password.grid(row=1, column=1, pady=10, padx=(0, 10))  

Button(root, text="Login", font=('Arial', 14)).grid(row=2, columnspan=2, pady=15)

result_label = Label(root, text="", fg="red", font=('Arial', 14))
result_label.grid(row=3, columnspan=2)

root.mainloop()
