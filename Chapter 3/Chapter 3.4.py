from tkinter import *

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        root.title("Shape Drawer")

        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        Label(self.root, text="Select Shape:").pack()

        self.shape_var = StringVar(value="oval")
        OptionMenu(self.root, self.shape_var, "oval", "rectangle", "square", "triangle").pack()

        Button(self.root, text="Draw Shape", command=self.draw_shape).pack(pady=10)

    def draw_shape(self):
        self.canvas.delete("all")  # Delete all the previous shapes drawn

        selected_shape = self.shape_var.get()

        if selected_shape == "oval":
            self.canvas.create_oval(50, 50, 350, 200, fill="lightblue")
        elif selected_shape == "rectangle":
            self.canvas.create_rectangle(50, 50, 350, 200, fill="lightgreen")
        elif selected_shape == "square":
            self.canvas.create_rectangle(50, 50, 200, 200, fill="lightcoral")
        elif selected_shape == "triangle":
            self.canvas.create_polygon(50, 200, 200, 50, 350, 200, fill="lightyellow")

if __name__ == "__main__":
    root = Tk()
    app = ShapeDrawer(root)
    root.mainloop()