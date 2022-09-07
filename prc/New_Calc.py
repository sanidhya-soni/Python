import imp
from tkinter import *
from unicodedata import name


class Calculator:
    def _init_(self):
        root.title("My Calculator")
        self.display = Entry(root, width=65, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.add_button = self.Buttons()

    def button_click(self, number):
        # self.display.delete(0, END)
        current = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, str(current) + str(number))

    def button_clear(self):
        self.display.delete(0, END)

    def button_add(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_equal(self):
        second_number = self.display.get()
        self.display.delete(0, END)
        if math == "addition":
            self.display.insert(0, f_num + int(second_number))
        elif math == "substraction":
            self.display.insert(0, f_num - int(second_number))
        elif math == "multiplication":
            self.display.insert(0, f_num * int(second_number))
        elif math == "division":
            self.display.insert(0, f_num / int(second_number))
        else:
            self.display.insert("error")

    def button_minus(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "substraction"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_mul(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_div(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.display.delete(0, END)

    def Buttons(self):
        button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: self.button_click(1))
        button_1.grid(row=3, column=0)
        button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: self.button_click(2))
        button_2.grid(row=3, column=1)
        button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: self.button_click(3))
        button_3.grid(row=3, column=2)
        button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: self.button_click(4))
        button_4.grid(row=2, column=0)
        button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: self.button_click(5))
        button_5.grid(row=2, column=1)
        button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: self.button_click(6))
        button_6.grid(row=2, column=2)
        button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: self.button_click(7))
        button_7.grid(row=1, column=0)
        button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: self.button_click(8))
        button_8.grid(row=1, column=1)
        button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: self.button_click(9))
        button_9.grid(row=1, column=2)
        button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: self.button_click(0))
        button_0.grid(row=4, column=0)
        button_plus = Button(root, text='+', padx=40, pady=20, command=self.button_add)
        button_plus.grid(row=4, column=1)
        button_minus = Button(root, text='-', padx=40, pady=20, command=self.button_minus)
        button_minus.grid(row=4, column=2)
        button_mul = Button(root, text='x', padx=40, pady=20, command=self.button_mul)
        button_mul.grid(row=5, column=0)
        button_div = Button(root, text='/', padx=40, pady=20, command=self.button_div)
        button_div.grid(row=5, column=1)
        button_clear = Button(root, text='clear', padx=40, pady=20, command=self.button_clear)
        button_clear.grid(row=5, column=2)
        button_eval = Button(root, text='=', padx=40, pady=20, command=self.button_equal)
        button_eval.grid(row=6, column=1)


if __name__ == '__main__':
    root = Tk()
    cal1 = Calculator()
    root.mainloop()
