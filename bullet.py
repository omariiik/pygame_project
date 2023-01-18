import pygame
from sprites_groups import wall_sprites
from sprites_groups import opponents_sprites
from game_map import map_board
from sprites_groups import player_sprite, Flag

class Bullet(pygame.sprite.Sprite):
    def __init__(self, px, py, x, y, name):
        pygame.sprite.Sprite.__init__(self)
        self.bullet = pygame.image.load("data/снаряд2.0.png").convert_alpha()
        self.image = self.bullet
        self.image_copy = self.image
        self.rect = self.bullet.get_rect()
        self.rect.x, self.rect.y = px, py
        self.x, self.y = x, y
        self.name = name
        self.op_dmg = 0

    def update(self, player):
        if self.rect.x < -65 or self.rect.x > 715 or self.rect.y < -65 or self.rect.y > 715:
            self.kill()
        if pygame.sprite.spritecollideany(self, opponents_sprites):
            if self.name == 'player':
                pygame.sprite.spritecollideany(self, opponents_sprites).health -= player.damage
            if pygame.sprite.spritecollideany(self, opponents_sprites).health <= 0:
                x, y = pygame.sprite.spritecollideany(self, opponents_sprites).number_cell()
                print(map_board[x][y])
                map_board[x][y] = 0
                print(map_board[x][y])
                pygame.sprite.spritecollideany(self, opponents_sprites).kill()
            if self.name == 'player':
                self.kill()
        if pygame.sprite.spritecollideany(self, player_sprite):
            if self.name == 'opponent':
                player.health -= self.op_dmg
            if player.health <= 0:
                player.kill()
                Flag = True
                pass
            if self.name == 'opponent':
                self.kill()
        if pygame.sprite.spritecollideany(self, wall_sprites):
            self.kill()
        if self.x == 1 or self.x == -1:
            self.rect.x += 2 * self.x
        if self.y == 1 or self.y == -1:
            self.rect.y += 2 * self.y

        # придумать проверку на столкновение нужно

    # def draw(self):
    #     pygame.draw.circle(screen, 'yellow', (self.px, self.py), 2)
        # можно не фото взять а рисовать , но замкнутый круг получится