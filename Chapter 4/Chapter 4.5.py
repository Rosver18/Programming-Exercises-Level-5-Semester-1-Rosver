from tkinter import *
from tkinter import messagebox

def validate_pass(password):
    
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special_char = any(char in "$#@!" for char in password)

    if (has_lowercase and has_digit and has_uppercase and has_special_char and
            6 <= len(password) <= 12):
        return True
    else:
        return False

def check_password():
    password = password_entry.get()

    if validate_pass(password):
        messagebox.showinfo("Success", "Password is valid!")
        root.destroy()  
    else:
        attempts_remaining = int(attempts_label.cget("text").split()[-1])
        if attempts_remaining > 1:
            attempts_label.config(text=f"Attempts remaining: {attempts_remaining - 1}")
        else:
            messagebox.showerror("Alert", "You ain't real! Get outta here!")
            root.destroy()  

root = Tk()
root.title("Password Validator")

password_label = Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = Entry(root, show="*")
password_entry.pack(pady=10)

check_button = Button(root, text="Check Password", command=check_password)
check_button.pack(pady=10)

attempts_label = Label(root, text="Attempts remaining: 5")
attempts_label.pack(pady=10)

root.mainloop()
