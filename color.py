from __future__ import annotations
# Color Palette Introductory Project
from tkinter import *
from tkinter import colorchooser
import colorsys
import random
from dataclasses import dataclass


def rand_color() -> Color:
    return Color(random.randint(0, 360), random.randint(0, 100), random.randint(0, 100))

def pick_color() -> Color:
    rgb = colorchooser.askcolor()[0]
    (h, s, v) = colorsys.rgb_to_hsv(rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0)
    hsv = Color(h * 360, s * 100, v * 100)
    return hsv
    

@dataclass(frozen=True)
class Color:
    h: int
    s: int
    v: int

    def to_tuple(self) -> tuple[int, int, int]:
        return self.h, self.s, self.v

    def hue_difference(self, difference) -> Color:
        return Color((self.h + difference) % 360, self.s, self.v)

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