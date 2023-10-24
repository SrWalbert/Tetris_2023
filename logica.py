import pygame

def exiting() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return running_program = False