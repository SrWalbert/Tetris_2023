"""Pygame es necesario para que no lance errores"""
import pygame

"""abc no ayuda con las abstracciones"""
from abc import ABC, abstractclassmethod

"""Random nos ayudará más tarde con la función choise"""
import random

"""Declarando funciones usadas en el archivo main2.py"""


def exititing() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False


def draw(list_: list[int], screen: tuple[int], pixel_size: int) -> pygame.Rect:
    for y, row in enumerate(list_):
        for x, pix in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if pix == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)


def collition() -> bool:
    # return allowed true or false
    pass


"""Declarando clases e instancias"""


# Clase madre piezas
class Piece(ABC):
    # def __init__(self, position: dict, shape: list[list[int]]) -> None:
    #     self.position: dict = position
    #     self.shape: list[list[int]] = shape
    @abstractclassmethod
    def __init__(self) -> None:
        self.position: list[int] = [1, 10]

    def __iter__(self):
        for row in self.shape:
            yield row

    @abstractclassmethod
    def rotate(self, allowed: bool):
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


# subclases de forma
class Cuadrade(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[1, 1], [1, 1]]

    def rotate(self):
        pass


class Linie(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[1, 1, 1, 1, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass


class LinieEle(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[1, 1, 1, 1], [0, 0, 0, 0, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass


class CuadradePlusOne(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[0, 1], [1, 1], [1, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass


class Crux(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

    def rotate(self):
        # no rotate
        pass


class CruxT(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: list[list[int]] = [[1, 1, 1], [0, 1, 0]]

    def rotate(self):
        # to rotate
        pass


cuadrade = Piece({"x": 5, "y": 5}, [[1, 1], [1, 1]])
linie = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1]])
linie_l = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1]])


actual_piece: Piece = random.choice([cuadrade, linie, linie_l])
