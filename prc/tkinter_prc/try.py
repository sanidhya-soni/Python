from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(1270, 720)

my_label = Label(text='I am a Label Ji', font=('Times New Roman', 24, 'italic'))
my_label.pack()



# Button


def button_clicked():
    text = input.get()
    my_label.config(text=text)


button = Button(text='Click Me', command=button_clicked)
button.pack()


# Entry

input = Entry(width=10)
input.pack()

print(input.get())



window.mainloop()
