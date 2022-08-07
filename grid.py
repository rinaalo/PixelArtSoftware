import pygame
import numpy as np

def Grid(col):

    blue = (190, 213, 235)
    white = (240, 240, 240)
    grey = (220, 220, 230)

    GRID_ROW = 32
    GRID_COL = 32
    WIDTH = 15
    HEIGHT = 15

    grid = np.arange(GRID_ROW * GRID_COL).reshape(GRID_ROW, GRID_COL)

    for row in range(GRID_ROW):
        for column in range(GRID_COL):
            grid[row][column] = 0

    pygame.init()
    window_size = [HEIGHT * GRID_COL + 100, WIDTH * GRID_ROW]
    surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()
    fps = 50
    pygame.key.set_repeat(10)

    # Game Loop
    run = True
    while run:
        click = pygame.mouse.get_pressed()
        clock.tick(fps)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            elif click[0]:
                pos = pygame.mouse.get_pos()
                column = pos[0] // WIDTH
                row = pos[1] // HEIGHT
                grid[row][column] = 1

        # Draw on Surface
        surface.fill(blue)
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                if (row + column) % 2 == 0:
                    color = white
                else:
                    color = grey
                if grid[row][column] == 1:
                    color = col
                pygame.draw.rect(surface, color, [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])
        
        pygame.display.flip()
    pygame.quit()