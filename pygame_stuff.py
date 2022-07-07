import pygame
import colorsys

SWATCH_WIDTH = 6
RECT_SIZE = 80
TEXT_HEIGHT = 15
FONT = pygame.font.SysFont("Helvetica", RECT_SIZE // 6)

def set_text(text):
    """Set font and text"""
    text_surface = FONT.render(text, False, (255, 255, 255))
    return text_surface

def x_offset(count):
    x = count % SWATCH_WIDTH * RECT_SIZE
    return x

def y_offset(count):
    y = count // SWATCH_WIDTH * RECT_SIZE
    return y

def start_pygame(colors):
    # Pygame junk
    pygame.init()
    # Prepare Screen
    # screensize = (min(SWATCH_WIDTH, len(colors)) * RECT_SIZE, (1 + len(colors) // SWATCH_WIDTH) * RECT_SIZE)
    screensize = (min(SWATCH_WIDTH, len(colors)) * RECT_SIZE, 6 * (RECT_SIZE + 15))

    # Set caption and clock rate
    pygame.display.set_caption("Color Palettes")
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(screensize)
    fps = 1




    # Game loop
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_g:
                    pass
        draw(colors, surface)
        pygame.display.update()
    pygame.quit()


def draw(colors, surface):
    surface.blit(set_text("Original Color:"), (0, y_offset(0)))
    for count, color in enumerate(colors[0:1]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + 15, RECT_SIZE, RECT_SIZE))
    # Complementary color
    surface.blit(set_text("Complementary Color:"), (0, y_offset(0) + (RECT_SIZE + TEXT_HEIGHT)))
    for count, color in enumerate(colors[0:2]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + RECT_SIZE + 30, RECT_SIZE, RECT_SIZE))
    # Analogous colors
    surface.blit(set_text("Analogous Colors:"), (0, y_offset(0) + 2 * (RECT_SIZE + TEXT_HEIGHT)))
    for count, color in enumerate(colors[2:5]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + 2 * (RECT_SIZE + 15) + 15, RECT_SIZE,
                                     RECT_SIZE))
    # Split complementary colors
    surface.blit(set_text("Split Complementary Colors:"), (0, y_offset(0) + 3 * (RECT_SIZE + TEXT_HEIGHT)))
    for count, color in enumerate(colors[5:8]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + 3 * (RECT_SIZE + 15) + 15, RECT_SIZE,
                                     RECT_SIZE))
    # Triad colors
    surface.blit(set_text("Triad Colors:"), (0, y_offset(count) + 4 * (RECT_SIZE + TEXT_HEIGHT)))
    for count, color in enumerate(colors[8:11]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + 4 * (RECT_SIZE + 15) + 15, RECT_SIZE,
                                     RECT_SIZE))
    # Tetradic colors
    surface.blit(set_text("Tetradic Colors:"), (0, y_offset(count) + 5 * (RECT_SIZE + TEXT_HEIGHT)))
    for count, color in enumerate(colors[11:15]):
        (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
        pygame.draw.rect(surface, (r * 255, g * 255, b * 255),
                         pygame.Rect(x_offset(count), y_offset(count) + 5 * (RECT_SIZE + 15) + 15, RECT_SIZE,
                                     RECT_SIZE))