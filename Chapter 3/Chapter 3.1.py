from tkinter import *

class GreetingApp:
    def __init__(self, root):
        self.root = root
        root.title("Greeting App")
        
        root.geometry("375x300")

        self.setup_input_frame()
        self.setup_display_frame()

    def setup_input_frame(self):
        self.input_frame = Frame(self.root, bg="lightblue", padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        Label(self.input_frame, text="Greeting App", fg="blue", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        Label(self.input_frame, text="Your Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = Entry(self.input_frame)
        self.name_entry.grid(row=1, column=1, pady=5, sticky="w")

        Label(self.input_frame, text="Select Color:").grid(row=2, column=0, sticky="w")
        self.color_var = StringVar(value="black")
        color_menu = OptionMenu(self.input_frame, self.color_var, "black", "red", "green", "blue")
        color_menu.grid(row=2, column=1, pady=5, sticky="w")

        Button(self.input_frame, text="Update Greeting", command=self.update_greeting).grid(row=3, column=0, columnspan=2, pady=10)

    def setup_display_frame(self):
        self.display_frame = Frame(self.root, bg="lightgreen", padx=10, pady=10)
        self.display_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.greeting_label = Label(self.display_frame, text="", font=("Arial", 12), bg="lightgreen")
        self.greeting_label.pack()

    def update_greeting(self):
        name = self.name_entry.get()
        selected_color = self.color_var.get()
        greeting = f"Hello, {name}!"
        self.greeting_label.config(text=greeting, fg=selected_color)

if __name__ == "__main__":
    root = Tk()
    app = GreetingApp(root)
    root.mainloop()
