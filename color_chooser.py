from tkinter import *
from tkinter import colorchooser

root = Tk()
root.geometry("400x400")

def pick_color():
    rgb = colorchooser.askcolor()
    r = Label(root, text=rgb[0][0]).pack(pady=10)
    g = Label(root, text=rgb[0][1]).pack(pady=10)
    b = Label(root, text=rgb[0][2]).pack(pady=10)


my_button = Button(root,text="Pick a Color",command=pick_color).pack()

root.mainloop()