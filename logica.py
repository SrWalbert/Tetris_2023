import pygame


def exitting() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False

def recorring(other_data_x, list_):
    for y, other_data_y in enumerate(list_):
        for x, other_data_x in enumerate(other_data_y):
        pass