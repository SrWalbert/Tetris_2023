import pygame
import random

def exititing() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False


class Piece:
    def __init__(self, position: dict, shape: list[list[int]]) -> None:
        self.position = position
        self.shape = shape

    def __iter__(self):
        for row in self.shape:
            yield row

    def draw(self, screen: tuple[int], pixel_size: int) -> pygame.Rect:
        for y, row_shape in enumerate(self.shape):
            for x, pix_shape in enumerate(row_shape):
                rect_shape = pygame.Rect(
                    (x + self.position["x"]) * pixel_size,
                    (y + self.position["y"]) * pixel_size,
                    pixel_size,
                    pixel_size,
                )
                if pix_shape == 0:
                    pygame.draw.rect(screen, (30, 30, 30), rect_shape)
                else:
                    pygame.draw.rect(screen, (250, 0, 0), rect_shape)


def draw(list_: list[int], screen: tuple[int], pixel_size: int) -> pygame.Rect:
    for y, row in enumerate(list_):
        for x, pix in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if pix == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)


#

#


cuadrade = Piece({"x": 5, "y": 5}, [[1, 1], [1, 1]])
linie = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1]])
linie_l = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1]])


actual_piece: Piece = random.choice([cuadrade, linie, linie_l])
