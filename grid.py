import pygame
import numpy as np

def Grid(col):

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    GRID_ROW = 32
    GRID_COL = 32
    WIDTH = 15
    HEIGHT = 15

    grid = np.arange(GRID_ROW * GRID_COL).reshape(GRID_ROW, GRID_COL)

    for row in range(GRID_ROW):
        for column in range(GRID_COL):
            grid[row][column] = 0

    pygame.init()
    window_size = [HEIGHT * GRID_COL, WIDTH * GRID_ROW]
    surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()
    fps = 50

    # Game Loop
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // WIDTH
                row = pos[1] // HEIGHT
                grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Draw on Surface
        surface.fill(black)
        for row in range(GRID_ROW):
            for column in range(GRID_COL):
                color = white
                if grid[row][column] == 1:
                    color = col
                pygame.draw.rect(surface, color, [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])
        
        pygame.display.flip()
    pygame.quit()