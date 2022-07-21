import color
from generate_colors import gen_colors
from pygame_stuff import start_pygame
from tkinter import *


def main():
    
    root = Tk()
    root.geometry("400x400")
    
    def color_chooser():
        col = color.pick_color()
        colors = gen_colors(col)
        start_pygame(colors)

    button = Button(root,text="Pick a Color",command=color_chooser)

    button.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
