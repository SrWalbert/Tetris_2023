import pygame
from abc import ABC, abstractmethod
import random
from cython.Build import cythonize

type board = list[list[int]]

offset_x, offset_y = 0, 0


@cythonize
def exititing() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False


@cythonize
def draw(list_: board, screen, pixel_size: int) -> pygame.Rect:
    for y, row in enumerate(list_):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if cell == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)


@cythonize
def move(piece: "Piece"):
    global offset_x, offset_y
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset_x = -1
            elif event.key == pygame.K_RIGHT:
                offset_x = 1
            elif event.key == pygame.K_DOWN:
                offset_y = 1

    if not collision(piece, (offset_x, offset_y)):
        piece.position[0] += offset_x
        piece.position[1] += offset_y

    offset_x, offset_y = 0, 0


def collision(piece: "Piece", offset: tuple[int, int]) -> bool:
    off_x, off_y = offset
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + piece.position[0] + off_x
                new_y = y + piece.position[1] + off_y
                if new_x < 0 or new_x >= len(board[0]) or new_y >= len(board):
                    return True
                if new_y >= 0 and board[new_y][new_x]:
                    return True
    return False


class Piece(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.position: list[int] = [0, 0]

    def __iter__(self):
        for row in self.shape:
            yield row

    @abstractmethod
    def rotate(self, allowed: bool):
        pass

    @abstractmethod
    def move(self, allowed: bool):
        pass


class Cuadrade(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1], [1, 1]]

    def rotate(self, allowed: bool):
        pass

    def move(self, allowed: bool):
        pass


class Linie(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1, 1, 1, 1]]

    def rotate(self, allowed: bool):
        pass

    def move(self, allowed: bool):
        pass


class LinieEle(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1, 1, 1], [0, 0, 0, 0, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


class CuadradePlusOne(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[0, 1], [1, 1], [1, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


class Crux(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

    def rotate(self):
        # no rotate
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


class CruxT(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1, 1], [0, 1, 0]]

    def rotate(self):
        # to rotate
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


class Z(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1, 0], [0, 1, 1]]

    def rotate(self):
        # to rotate
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


