import sys
import pygame

def run_game():
    pygame.init()
    sc = pygame.display.set_mode((400, 450))
    bg_color = (220, 220, 255)
    sc.fill(bg_color)
    # здесь будут рисоваться фигуры
    pygame.draw.rect(sc, (156, 55, 0), (50, 20, 10, 375))
    # белая часть фигуры
    pygame.draw.rect(sc, (255, 255, 255), (52, 20, 300, 60))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()