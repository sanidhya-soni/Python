from tkinter import *
import math
import numpy as np


# Function to add in the entry of text display
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)


# Funtion to find the result of an operation
def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op


tk_calc = Tk()
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input, justify='right').grid(columnspan=5, padx = 10, pady = 15)

button_params = {'font':('sans-serif', 20, 'bold')}


button_7 = Button(tk_calc, button_params, text='7',
                  command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button_8 = Button(tk_calc, button_params, text='8',
                  command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button_9 = Button(tk_calc, button_params, text='9',
                  command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
delete_one = Button(tk_calc, button_params, text='DEL',
                  command=button_delete).grid(row=6, column=3, sticky="nsew")
delete_all = Button(tk_calc, button_params, text='AC',
                  command=button_clear_all).grid(row=6, column=4, sticky="nsew")


button_4 = Button(tk_calc, button_params, text='4',
                  command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button_5 = Button(tk_calc, button_params, text='5',
                  command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button_6 = Button(tk_calc, button_params, text='6',
                  command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
mul = Button(tk_calc, button_params, text='*',
             command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(tk_calc, button_params, text='/',
             command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")


button_1 = Button(tk_calc, button_params, text='1',
                  command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button_2 = Button(tk_calc, button_params, text='2',
                  command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button_3 = Button(tk_calc, button_params, text='3',
                  command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(tk_calc, button_params, text='+',
             command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(tk_calc, button_params, text='-',
             command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")


button_0 = Button(tk_calc, button_params, text='0',
                  command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
point = Button(tk_calc, button_params, text='.',
               command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
exp = Button(tk_calc, button_params, text='EXP', font=('sans-serif', 16, 'bold'),
             command=lambda:button_click(E)).grid(row=9, column=2, sticky="nsew")
equal = Button(tk_calc, button_params, text='=',
               command=button_equal).grid(row=9, columnspan=2, column=3, sticky="nsew")


tk_calc.mainloop()
