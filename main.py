import color
from generate_colors import gen_colors
from pygame_stuff import start_pygame
import grid
from tkinter import *


def main():
    
    '''
    root = Tk()
    root.geometry("400x400")
    
    def color_chooser():
        #hsv = color.hsv_color()
        rgb = color.rgb_color()
        grid.Grid(rgb)
        #colors = gen_colors(hsv)
        #start_pygame(colors)

    button = Button(root,text="Pick a Color",command=color_chooser)

    button.pack()
    root.mainloop()
    '''
    # TODO 
    # fix the color choosing thing
    # make a main menu that will let the user pick canvas size
    # the canvas should have the pick color and show palette option
    # an eraser
    # brush size
    # brush options?
    # undo
    # redo?
    # save files
    # LAYERS ?
    # menu bar
    # use icons for the buttons, looks cute    

    grid.Grid()


if __name__ == '__main__':
    main()
