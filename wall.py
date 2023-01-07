import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.wall = pygame.image.load("data/стена.png").convert_alpha()
        self.image = self.wall
        self.rect = self.wall.get_rect()