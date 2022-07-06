from __future__ import annotations
# Color Palette Introductory Project
import pygame
import colorsys
import random
from dataclasses import dataclass

SWATCH_WIDTH = 6
RECT_SIZE = 90
    
def start_pygame(colors):
    # Pygame junk
    pygame.init()
    # Prepare Screen
    screensize = (min(SWATCH_WIDTH, len(colors)) * RECT_SIZE, (1 + len(colors) // SWATCH_WIDTH) * RECT_SIZE)
    # Set caption
    pygame.display.set_caption("Color Palettes")
    #clock = pygame.time.Clock()
    surface = pygame.display.set_mode(screensize)
    #fps = 1

    # Game loop
    run = True
    while run:
        #clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                elif event.key == pygame.K_g:
                    pass
        
        for count, color in enumerate(colors):
            x_offset = count % SWATCH_WIDTH * RECT_SIZE
            y_offset = count // SWATCH_WIDTH * RECT_SIZE
            (r, g, b) = colorsys.hsv_to_rgb(color.h / 360.0, color.s / 100.0, color.v / 100.0)
            pygame.draw.rect(surface, (r * 255, g * 255, b * 255), pygame.Rect(x_offset, y_offset, RECT_SIZE, RECT_SIZE))
        pygame.display.update()
    pygame.quit()

@dataclass(frozen=True)
class Color:
    h: int
    s: int
    v: int

    def to_tuple(self) -> tuple(int, int, int):
        return (self.h, self.s, self.v)

    # def hsv_to_rgb(self) -> tuple(int, int, int):
    #     r, g, b: int, int, int
    #     if 0 <= self.h < 60:
    #         r = 255 * self.v
    #         g = 
    #     return (self.h, self.s, self.v)

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
    col = Color.rand_color() # C
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
    print(colors)

if __name__ == '__main__':
    main()