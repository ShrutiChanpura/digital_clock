from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("")
window.configure(bg="white")
window.resizable(False, False)

clock_label = Label(window, bg = "white", fg ="black", font = ("Times",30),relief='flat')
clock_label.place(x=20, y=20)

def update_label():
    current_time= strftime('%H: %M :%S ')
    clock_label.configure(text= current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()
