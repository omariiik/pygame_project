import pygame
# from main import screen
pygame.init()

def show_go_screen():
    good_bye = pygame.image.load("data/gameover.png")
    clock = pygame.time.Clock()
    x = -650
    y = 0
    if x < 0:
        x += 30
        screen.blit(good_bye, (x, y))