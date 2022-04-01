from tkinter import *
#from decimal import *


class Calculator(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.build()

    def build(self):
        btns = [
            "C", "DEL", "X^2", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "+/-", "0", "%", "*"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#faf0e6",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"),
                         bg="#faf0e6", foreground="#000")
        self.lbl.place(x=11, y=50)

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula, bg="#FFF")


if __name__ == '__main__':

    root = Tk()
    root.title('Calculator')
    root.geometry("485x550+300+300")
    root.resizable(0,0)
    app = Calculator(root)
    app.pack()
    root.mainloop()





