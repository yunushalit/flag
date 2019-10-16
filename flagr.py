import sys
import pygame

def run_game():
    pygame.init()
    sc = pygame.display.set_mode((400, 450))
    bg_color = (220, 220, 255)
    sc.fill(bg_color)

    # флэшток фигуры
    pygame.draw.rect(sc, (255, 155, 0), (52, 18, 10, 420))
    # белая часть фигуры
    pygame.draw.rect(sc, (255, 255, 255), (52, 20, 340, 80))

    # Синяя часть фигуры
    pygame.draw.rect(sc, (0, 0, 255), (52, 100, 340, 80))

    # красная часть фигуры
    pygame.draw.rect(sc, (255, 55, 0), (52, 180, 340, 80))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()