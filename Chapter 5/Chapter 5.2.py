from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def calcGrade(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        return avg
    
    def display(self):
        avg = self.calcGrade()
        return f"Hello {self.name}! Your average grade is {avg}. Congratulations!"

class StudentGUI(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Student Information")
        self.geometry("300x200")
        
        self.input_values()
    
    def input_values(self):
        labels = ["Name:", "Mark 1:", "Mark 2:", "Mark 3:"]
        entries = [Entry(self, width=20) for _ in range(4)]

        for i in range(4):
            Label(self, text=labels[i]).grid(row=i, column=0, pady=5, padx=5, sticky=W)
            entries[i].grid(row=i, column=1, pady=5, padx=5)

        def calculate_grade():
            name = entries[0].get()
            mark1 = int(entries[1].get())
            mark2 = int(entries[2].get())
            mark3 = int(entries[3].get())
            
            student = Student(name, mark1, mark2, mark3)
            result_label = messagebox.showinfo("Result", message=student.display())

        calculate_button = Button(self, text="Calculate Grade", command=calculate_grade)
        calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
        
if __name__ == "__main__":
    app = StudentGUI()
    app.mainloop()
