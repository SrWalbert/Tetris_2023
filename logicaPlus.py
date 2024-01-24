"""Pygame es necesario para que no lance errores"""
import pygame

"""abc no ayuda con las abstracciones"""
from abc import ABC, abstractclassmethod

"""Random nos ayudará más tarde con la función choise"""
import random

# """Compila una función de python, no es óptimo, pero es útil"""
# from cython import Cythonize

"""Declarando tipos de datos"""
type board = list[list[int,],]
"""Declarando funciones usadas en el archivo main2.py"""


# @Cythonize
def exititing() -> bool:
    """Salir de la aplicación

    Returns:
        bool: True, sigue corriendo, False, se termina el loop
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


# @Cythonize
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
