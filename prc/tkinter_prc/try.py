import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(1270, 720)

my_label = tkinter.Label(text='I am a Label Ji', font=('Times New Roman', 24, 'italic'))
my_label.pack()


window.mainloop()
