"""Pygame es necesario para que no lance errores"""
import pygame

"""abc no ayuda con las abstracciones"""
from abc import ABC, abstractclassmethod

"""Random nos ayudará más tarde con la función choise"""
import random

"""Compila una función de python, no es óptimo, pero es útil"""
from cython.Build import Cythonize

"""Declarando tipos de datos"""
type board = list[list[int]]
"""Declarando funciones usadas en el archivo main2.py"""

"Asignado variables de offset para movimientos"
offset_x, offset_y:int = 0, 0
offset = offset_x, offset_y


@Cythonize
def exititing() -> bool:
    """Salir de la aplicación

    Returns:
        bool: True, sigue corriendo, False, se termina el loop
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False


@Cythonize
def draw(list_: board, screen: tuple[int], pixel_size: int) -> pygame.Rect:
    """Dibuja las figuras en pantalla

    Args:
        list_ (board): Lista que contiene los datos de poscición de todo
        screen (tuple[int]): Datos por defecto de la ventana
        pixel_size (int): Tamaño del botón dado por defecto

    Returns:
        pygame.Rect: Dibujo grafico en la pantalla
    """
    for y, row in enumerate(list_):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if cell == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)




def move():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                offset_x = -1  # Mover a la izquierda
            elif event.key == pygame.K_RIGHT:
                offset_x = 1  # Mover a la derecha
            elif event.key == pygame.K_DOWN:
                offset_y = 1  # Mover hacia abajo
    return offset

# Después, usas offset_x y offset_y para mover tu pieza y comprobar colisiones


def collition() -> bool:
    """
    Comprueba si hay una colisión entre la pieza y otras piezas o los bordes del tablero.

    Args:
    board (list of list of int): El tablero del juego.
    piece (Piece): La pieza actual que se está moviendo o rotando.
    offset (tuple of int): El desplazamiento (dx, dy) para la pieza.

    Returns:
    bool: True si hay una colisión, False en caso contrario.
    """
    off_x, off_y = offset
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + off_x
                new_y = y + off_y
                # Comprobar si está fuera del tablero (lados, abajo)
                if new_x < 0 or new_x >= len(board[0]) or new_y >= len(board):
                    return True
                # Comprobar si la posición ya está ocupada
                if new_y >= 0 and board[new_y][new_x]:
                    return True
    return False


"""Declarando clases e instancias"""


# Clase madre piezas
class Piece(ABC):
    # def __init__(self, position: dict, shape: board) -> None:
    #     self.position: dict = position
    #     self.shape: board = shape
    @abstractclassmethod
    def __init__(self) -> None:
        self.position: list[int] = [1, 10]

    def __iter__(self):
        for row in self.shape:
            yield row

    @abstractclassmethod
    def rotate(self, allowed: bool):
        pass

    @abstractclassmethod
    def move(self, allowed: bool):
        if allowed:
            pass


# subclases de forma
class Cuadrade(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1], [1, 1]]

    def rotate(self):
        pass

    def move(self, allowed: bool):
        if allowed:
            pass


class Linie(Piece):
    def __init__(self) -> None:
        super().__init__()
        self.shape: board = [[1, 1, 1, 1, 1]]

    def rotate(self, allowed: bool):
        # To rotate
        pass

    def move(self, allowed: bool):
        if allowed:
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


if __name__ == "__main__":
    cuadrade = Piece({"x": 5, "y": 5}, [[1, 1], [1, 1]])
    linie = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1]])
    linie_l = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1]])

    actual_piece: Piece = random.choice([cuadrade, linie, linie_l])
