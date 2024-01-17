from tkinter import *

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "Addition": result = num1 + num2
        elif operation == "Subtraction": result = num1 - num2
        elif operation == "Multiplication": result = num1 * num2
        elif operation == "Division": result = num1 / num2
        elif operation == "Modulo Division": result = num1 % num2
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = Tk()
root.title("Calculator")
root.geometry("400x400")

entry_num1 = Entry(root, width=10, font=('Arial', 14))
entry_num2 = Entry(root, width=10, font=('Arial', 14))

result_label = Label(root, text="Result:", font=('Arial', 14, 'bold'))

operation_var = StringVar(value="Addition")
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]

operation_frame = Frame(root)
operation_frame.pack(pady=5)

for operation in operations:
    Radiobutton(operation_frame, text=operation, variable=operation_var, value=operation, font=('Arial', 12)).pack(side=TOP, pady=5)

Button(root, text="Calculate", command=calculate, font=('Arial', 14)).pack(pady=10)

entry_num1.pack(pady=5)
entry_num2.pack(pady=5)
result_label.pack()

root.mainloop()
