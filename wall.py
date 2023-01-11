import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.wall = pygame.image.load("data/стена.png").convert_alpha()
        self.image = self.wall
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y