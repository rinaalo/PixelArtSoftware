from color import *
import pygame
import numpy as np

def Grid():

    # Set color
    blue = (190, 213, 235)
    white = (240, 240, 240)
    grey = (220, 220, 230)
    black = (0, 0, 0)
    current_color = black

    GRID_ROW = 32
    GRID_COL = 32

    if GRID_ROW <= 40 or GRID_COL <= 40:
        WIDTH = 15
        HEIGHT = 15
    elif (GRID_ROW > 40 and GRID_ROW <= 64) or (GRID_COL > 40 and GRID_COL <= 64):
        WIDTH = 10
        HEIGHT = 10
    else:
        WIDTH = 7
        HEIGHT = 7

    MENU = 100

    grid = np.arange(GRID_ROW * GRID_COL, dtype=Color).reshape(GRID_ROW, GRID_COL)

    for row in range(GRID_ROW):
        for column in range(GRID_COL):
            grid[row][column] = 0

    pygame.init()
    window_size = [WIDTH * GRID_COL + MENU, HEIGHT * GRID_ROW]
    surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()
    fps = 200

    #Alpha Layer
    layer = pygame.Surface((window_size))
    layer.set_alpha(0)
    layer.fill((255, 255, 255))
    surface.blit(layer, (0,0))

    # Buttons
    menu_width = MENU
    menu_height = HEIGHT * GRID_ROW

    colors_textcolor = (0, 0, 0)
    colors_lightcolor = (150, 150, 150)
    colors_darkcolor = (60, 60, 60)

    font = pygame.font.SysFont('Corbel', MENU // 4)
    colors_text = font.render('Colors', True , colors_textcolor)

    # Draw on canvas
    def render_canvas(new_color):
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                if grid[row][column] != 0:
                    pygame.draw.rect(surface, grid[row][column],
                    [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])
                else:
                    pygame.draw.rect(layer, grid[row][column],
                    [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])


    # Game Loop
    run = True
    while run:
        click = pygame.mouse.get_pressed()
        clock.tick(fps)
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            # Click on canvas
            if click[0]:
                column = pos[0] // WIDTH
                row = pos[1] // HEIGHT
                try:
                    grid[row][column] = current_color
                except IndexError:
                    pass
            # Click on button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_width/6 + (WIDTH * GRID_COL) <= pos[0] <= menu_width/2 + (WIDTH * GRID_COL) and menu_height/6 <= pos[1] <= menu_height/4:
                    current_color = rgb_color()
                
        surface.fill(blue)

        # Blank canvas
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                if (row + column) % 2 == 0:
                    color = white
                else:
                    color = grey
                pygame.draw.rect(surface, color, [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])

        # Draw on canvas
        #alpha_layer()
        render_canvas(current_color)

        # Button Color
        try:
            if current_color != black:
                button_color = current_color
            else:
                button_color = grey
        except UnboundLocalError:
            button_color = colors_darkcolor

        # Create Buttons
        if menu_width/6 + (WIDTH * GRID_COL) <= pos[0] <= menu_width/2 + (WIDTH * GRID_COL) and menu_height/6 <= pos[1] <= menu_height/4:
            pygame.draw.rect(surface,colors_lightcolor,[menu_width/6 + (WIDTH * GRID_COL),menu_height/6, menu_width - menu_width/5, menu_height/12])
        else:
            pygame.draw.rect(surface,button_color,[menu_width/6 + (WIDTH * GRID_COL),menu_height/6, menu_width - menu_width/5, menu_height/12])

        surface.blit(colors_text , (menu_width/6 + (WIDTH * GRID_COL),menu_height/6))

        pygame.display.flip()    
    pygame.quit()