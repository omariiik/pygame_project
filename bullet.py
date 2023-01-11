import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, px, py, dx, dy):
        pygame.sprite.Sprite.__init__(self)
        self.bullet = pygame.image.load("data/###.png").convert_alpha() # найти фото нужно
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > 650 or self.py < 0 or self.py > 650:
            self.bullet.remove(self)
        # придумать проверку на столкновение нужно

    # def draw(self):
    #     pygame.draw.circle(screen, 'yellow', (self.px, self.py), 2)
        # можно не фото взять а рисовать , но замкнутый круг получится