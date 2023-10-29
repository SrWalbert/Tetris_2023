import pygame


def exititing() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return False


def draw(list_: list[int], screen: tuple, pixel_size: int) -> pygame.Rect:
    for y, row in enumerate(list_):
        for x, pix in enumerate(row):
            rect = pygame.Rect(x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            if pix == 0:
                pygame.draw.rect(screen, (30, 30, 30), rect)
            else:
                pygame.draw.rect(screen, (107, 52, 118), rect)
