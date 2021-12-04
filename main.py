from tkinter import *
from time import strftime

root = Tk()
root.title("L33th - PyClock")


def time():
    string = strftime('%H:%M:%S %P')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("us-digital", 80), background="black", foreground="green")
label.pack(anchor='center')

time()

mainloop()
