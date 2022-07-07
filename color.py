from __future__ import annotations
# Color Palette Introductory Project

import random
from dataclasses import dataclass


def rand_color() -> Color:
    return Color(random.randint(0, 360), random.randint(0, 100), random.randint(0, 100))


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