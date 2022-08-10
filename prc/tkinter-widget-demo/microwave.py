from tkinter import *

window = Tk()
window.minsize(width=1280, height=720)

my_label = Label(text='Microwave Oven', font=('Times New Roman', 30, 'italic'))
my_label.pack()

# Select your food
food = ['Pizza', 'Fries', 'Chicken', 'Make some Food Warm']
listbox = Listbox(height=len(food), width=30)
for item in food:
    listbox.insert(food.index(item), item)

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()

window.mainloop()
