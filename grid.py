from color import *
from generate_colors import gen_colors
import pygame
import numpy as np

def Grid():

    # Set color
    blue = (190, 213, 235)
    white = (240, 240, 240)
    grey = (220, 220, 230)
    black = (0, 0, 0)
    current_color = black

    SCREEN_WIDTH = 512
    SCREEN_HEIGHT = 512
    MENU_WIDTH_OFFSET = 100

    GRID_ROW = 32
    GRID_COL = 32

    PIXEL_WIDTH = SCREEN_WIDTH // GRID_COL
    PIXEL_HEIGHT = SCREEN_HEIGHT // GRID_ROW

    grid = np.arange(GRID_ROW * GRID_COL, dtype=Color).reshape(GRID_ROW, GRID_COL)

    for row in range(GRID_ROW):
        for column in range(GRID_COL):
            grid[row][column] = 0

    pygame.init()
    window_size = [SCREEN_WIDTH + MENU_WIDTH_OFFSET, SCREEN_HEIGHT]
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
    menu_width = MENU_WIDTH_OFFSET
    menu_height = PIXEL_HEIGHT * GRID_ROW

    colors_lightcolor = (150, 150, 150)
    colors_darkcolor = (60, 60, 60)

    font = pygame.font.SysFont('Corbel', MENU_WIDTH_OFFSET // 4)

    # Draw on canvas
    def render_canvas(new_color):
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                if grid[row][column] != 0:
                    pygame.draw.rect(surface, grid[row][column],
                    [PIXEL_WIDTH * column, PIXEL_HEIGHT * row, PIXEL_WIDTH, PIXEL_HEIGHT])
                else:
                    pygame.draw.rect(layer, grid[row][column],
                    [PIXEL_WIDTH * column, PIXEL_HEIGHT * row, PIXEL_WIDTH, PIXEL_HEIGHT])


    # Game Loop
    run = True
    while run:
        click = pygame.mouse.get_pressed()
        clock.tick(fps)
        pos = pygame.mouse.get_pos()

        colors_textcolor = (255 - current_color[0], 255 - current_color[1], 255 - current_color[2])
        colors_text = font.render('Colors', True , colors_textcolor)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            # Click on canvas
            if click[0]:
                column = pos[0] // PIXEL_WIDTH
                row = pos[1] // PIXEL_HEIGHT
                try:
                    grid[row][column] = current_color
                except IndexError:
                    pass
            # Click on button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_width/6 + (PIXEL_WIDTH * GRID_COL) <= pos[0] <= menu_width/2 + (PIXEL_WIDTH * GRID_COL) and menu_height/6 <= pos[1] <= menu_height/4:
                    temporary_color = rgb_color()
                    if (temporary_color != None): current_color = temporary_color 
                
        surface.fill(blue)

        # Blank canvas
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                if (row + column) % 2 == 0:
                    color = white
                else:
                    color = grey
                pygame.draw.rect(surface, color, [PIXEL_WIDTH * column, PIXEL_HEIGHT * row, PIXEL_WIDTH, PIXEL_HEIGHT])

        # Draw on canvas
        #alpha_layer()
        render_canvas(current_color)

        # Button Color
        try:
            button_color = current_color
        except UnboundLocalError:
            button_color = colors_darkcolor

        # Create Buttons
        if menu_width/6 + (PIXEL_WIDTH * GRID_COL) <= pos[0] <= menu_width/2 + (PIXEL_WIDTH * GRID_COL) and menu_height/6 <= pos[1] <= menu_height/4:
            pygame.draw.rect(surface,colors_lightcolor,[menu_width/6 + (PIXEL_WIDTH * GRID_COL),menu_height/6, menu_width - menu_width/5, menu_height/12])
        else:
            pygame.draw.rect(surface,button_color,[menu_width/6 + (PIXEL_WIDTH * GRID_COL),menu_height/6, menu_width - menu_width/5, menu_height/12])

        surface.blit(colors_text , (menu_width/6 + (PIXEL_WIDTH * GRID_COL),menu_height/6))

        pygame.display.flip()    
    pygame.quit()