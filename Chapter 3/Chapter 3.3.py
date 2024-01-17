from tkinter import *
from tkinter import ttk
import math

class AreaCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Area Calculator")

        
        root.geometry("400x300")

        self.setup_tabs()

    def setup_tabs(self):
        tab_control = ttk.Notebook(self.root)

        circle_tab = ttk.Frame(tab_control)
        square_tab = ttk.Frame(tab_control)
        rectangle_tab = ttk.Frame(tab_control)

        tab_control.add(circle_tab, text="Circle")
        tab_control.add(square_tab, text="Square")
        tab_control.add(rectangle_tab, text="Rectangle")

        self.setup_circle_tab(circle_tab)
        self.setup_square_tab(square_tab)
        self.setup_rectangle_tab(rectangle_tab)

        tab_control.pack(expand=1, fill="both")

    def setup_circle_tab(self, circle_tab):
        Label(circle_tab, text="Enter the radius:").pack(pady=10)
        self.radius_entry = Entry(circle_tab)
        self.radius_entry.pack(pady=10)

        Button(circle_tab, text="Calculate Area", command=self.calculate_circle_area).pack(pady=10)

        self.circle_result_label = Label(circle_tab, text="")
        self.circle_result_label.pack(pady=10)

    def setup_square_tab(self, square_tab):
        Label(square_tab, text="Enter the side length:").pack(pady=10)
        self.side_length_entry = Entry(square_tab)
        self.side_length_entry.pack(pady=10)

        Button(square_tab, text="Calculate Area", command=self.calculate_square_area).pack(pady=10)

        self.square_result_label = Label(square_tab, text="")
        self.square_result_label.pack(pady=10)

    def setup_rectangle_tab(self, rectangle_tab):
        Label(rectangle_tab, text="Enter the length:").pack(pady=10)
        self.length_entry = Entry(rectangle_tab)
        self.length_entry.pack(pady=10)

        Label(rectangle_tab, text="Enter the width:").pack(pady=10)
        self.width_entry = Entry(rectangle_tab)
        self.width_entry.pack(pady=10)

        Button(rectangle_tab, text="Calculate Area", command=self.calculate_rectangle_area).pack(pady=10)

        self.rectangle_result_label = Label(rectangle_tab, text="")
        self.rectangle_result_label.pack(pady=10)

    def calculate_circle_area(self):
        try:
            radius = float(self.radius_entry.get())
            area = math.pi * radius**2
            self.circle_result_label.config(text=f"Area: {area:.2f} square units")
        except ValueError:
            self.circle_result_label.config(text="Invalid input. Enter a numeric value.")

    def calculate_square_area(self):
        try:
            side_length = float(self.side_length_entry.get())
            area = side_length**2
            self.square_result_label.config(text=f"Area: {area:.2f} square units")
        except ValueError:
            self.square_result_label.config(text="Invalid input. Enter a numeric value.")

    def calculate_rectangle_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            self.rectangle_result_label.config(text=f"Area: {area:.2f} square units")
        except ValueError:
            self.rectangle_result_label.config(text="Invalid input. Enter numeric values.")

if __name__ == "__main__":
    root = Tk()
    app = AreaCalculator(root)
    root.mainloop()
