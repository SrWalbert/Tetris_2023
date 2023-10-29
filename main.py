import time
import pygame
import random

pygame.init()

SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board: list[int] = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
pixel_size: int = 30  # Tamaño de cada cuadrado en píxeles


# Piezas
class Piece:
    def __init__(self, position: dict, shape: list[list[int]]) -> None:
        self.position = position
        self.shape = shape

    def __iter__(self):
        for row in self.shape:
            yield row


cuadrade = Piece({"x": 5, "y": 5}, [[1, 1], [1, 1]])
linie = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1]])
linie_l = Piece({"x": 5, "y": 5}, [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1]])


actual_piece: Piece = random.choice([cuadrade, linie, linie_l])


# Dibujar la cuadricula
def draw() -> pygame.Rect():
    pixel_size: int = 30  # Tamaño de cada cuadrado en píxeles

    for y, row in enumerate(board):
        for x, pix in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if pix == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)

    # Dubujar pieza

    # Recordar cambiar cuadrade por piece
    for y, row_shape in enumerate(actual_piece):
        for x, pix_shape in enumerate(row_shape):
            rect_shape = pygame.Rect(
                (x + actual_piece.position["x"]) * pixel_size,
                (y + actual_piece.position["y"]) * pixel_size,
                pixel_size,
                pixel_size,
            )
            if pix_shape == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect_shape)
            else:
                pygame.draw.rect(screen, (250, 0, 0), rect_shape)


# def rotation():


# Colisión con otros pixeles o con los muros
def collition() -> bool:
    for y, row in enumerate(board):
        for x, pix in enumerate(row):
            if y == row[19]:
                return False
            if x < pix[0] or x > pix[19]:
                return False
            # Falta saber si hay otros bloques cerca
            else:
                return True


def falling(allowed: bool):
    while allowed:
        actual_piece.position["y"] = actual_piece.position["y"] + 1
        time.sleep(1)


# Qué es estar congelado


def move(allowed: bool):
    if allowed == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_s:
                actual_piece.position["y"] = actual_piece.position["y"] + 1
            if event.key == pygame.k_a:
                actual_piece.position["x"] = actual_piece.position["x"] - 1
            if event.key == pygame.k_d:
                actual_piece.position["x"] = actual_piece.position["x"] + 1
    falling(allowed)


run = True
while run:
    draw()

    # Salir del juego
    for event in pygame.event.get():
        move(collition())
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
