from __future__ import annotations
# Color Palette Introductory Project
import pygame
import colorsys
import random
from dataclasses import dataclass

SWATCH_WIDTH = 6
RECT_SIZE = 80
    
def start_pygame(colors):
    # Pygame junk
    pygame.init()
    # Prepare Screen
    #screensize = (min(SWATCH_WIDTH, len(colors)) * RECT_SIZE, (1 + len(colors) // SWATCH_WIDTH) * RECT_SIZE)
    screensize = (min(SWATCH_WIDTH, len(colors)) * RECT_SIZE, 6*(RECT_SIZE + 15))

    # Set caption and clock rate
    pygame.display.set_caption("Color Palettes")
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(screensize)
    fps = 1

    # Set font and text
    my_font = pygame.font.SysFont("Helvetica", RECT_SIZE // 6)

    def set_text(text):
        text_surface = my_font.render(text, False, (255, 255, 255))
        return text_surface

    # Set coordinates
    def x_offset(count):
        x = count % SWATCH_WIDTH * RECT_SIZE
        return x

    def y_offset(count):
        y = count // SWATCH_WIDTH * RECT_SIZE
        return y

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
        
        # Original color
        surface.blit(set_text("Original Color:"), (0, y_offset(0)))
        for count, color in enumerate(colors[0:1]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + 15, RECT_SIZE, RECT_SIZE))

        # Complementary color
        surface.blit(set_text("Complementary Color:"), (0, y_offset(0) + (RECT_SIZE + 15)))
        for count, color in enumerate(colors[0:2]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + RECT_SIZE + 30, RECT_SIZE, RECT_SIZE))

        # Analogous colors
        surface.blit(set_text("Analogous Colors:"), (0, y_offset(0) + 2*(RECT_SIZE + 15)))
        for count, color in enumerate(colors[2:5]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + 2*(RECT_SIZE + 15) + 15, RECT_SIZE, RECT_SIZE))

        # Split complementary colors
        surface.blit(set_text("Split Complementary Colors:"), (0, y_offset(0) + 3*(RECT_SIZE + 15)))
        for count, color in enumerate(colors[5:8]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + 3*(RECT_SIZE + 15) + 15, RECT_SIZE, RECT_SIZE))

        # Triad colors
        surface.blit(set_text("Triad Colors:"), (0, y_offset(count) + 4*(RECT_SIZE + 15)))
        for count, color in enumerate(colors[8:11]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + 4*(RECT_SIZE + 15) + 15, RECT_SIZE, RECT_SIZE))

        # Tetradic colors
        surface.blit(set_text("Tetradic Colors:"), (0, y_offset(count) + 5*(RECT_SIZE + 15)))
        for count, color in enumerate(colors[11:15]):
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset(count), y_offset(count) + 5*(RECT_SIZE + 15) + 15, RECT_SIZE, RECT_SIZE))

        pygame.display.update()
    pygame.quit()

@dataclass(frozen=True)
class Color:
    h: int
    s: int
    v: int

    def to_tuple(self) -> tuple(int, int, int):
        return (self.h, self.s, self.v)

    def hue_difference(self, difference) -> Color:
        return Color((self.h + difference) % 360, self.s, self.v)

    def rand_color() -> Color:
        return Color(random.randint(0, 360), random.randint(0, 100), random.randint(0, 100))

    def complementary_color(self) -> Color:
        return Color((self.h + 180) % 360, self.s, self.v)

    def analogous_color(self, order) -> Color:
        return Color((self.h + 30 * order) % 360, self.s, self.v)

    def split_complementary_color(self, order) -> Color:
        return Color((((self.h + 30 * order) % 360) + 180) % 360, self.s, self.v)

    def triad_color(self, order) -> Color:
        return Color((((self.h + 60 * order) % 360) + 180) % 360, self.s, self.v)
    
    def tetradic_color(self, order) -> Color:
        return Color((self.h + 60 * order) % 360, self.s, self.v)


def main():
    # generate colors
    col = Color.rand_color() 
    complement = col.complementary_color()

    analogous = []
    analogous.append(col.analogous_color(0))
    analogous.append(col.analogous_color(1))
    analogous.append(col.analogous_color(-1))

    split_complement = []
    split_complement.append(col)
    split_complement.append(col.split_complementary_color(1))
    split_complement.append(col.split_complementary_color(-1))

    triad = []
    triad.append(col)
    triad.append(col.triad_color(1))
    triad.append(col.triad_color(-1))

    tetradic = []
    tetradic.append(col.tetradic_color(0))
    tetradic.append(col.tetradic_color(1))
    tetradic.append(col.tetradic_color(3))
    tetradic.append(col.tetradic_color(-2))

    print("Color: ", col)
    print("Complement: ", complement)
    print("Analogous: ", analogous)
    print("Split complement: ", split_complement)
    print("Triad: ", triad)
    print("Tetradic: ", tetradic)

    colors = [col] + [complement] + analogous + split_complement + triad + tetradic
    start_pygame(colors)

if __name__ == '__main__':
    main()
