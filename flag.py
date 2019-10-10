import sys
import pygame

def run_game():
    pygame.init()
    sc = pygame.display.set_mode((400, 450))
    bg_color = (220, 220, 255)
    sc.fill(bg_color)
    # флэшток фигуры
    pygame.draw.rect(sc, (155, 55, 0), (50, 20, 10, 360))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()