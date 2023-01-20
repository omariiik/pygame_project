import pygame
from sprites_groups import wall_sprites
from sprites_groups import opponents_sprites
from generation_map import map_board
from sprites_groups import player_sprite
from music import dead_player, dead_opponent
from sprites_groups import bullet_group

class Bullet(pygame.sprite.Sprite):
    def __init__(self, px, py, x, y, name, dad):
        pygame.sprite.Sprite.__init__(self)
        self.bullet = pygame.image.load("data/снаряд2.0.png").convert_alpha()
        self.image = self.bullet
        self.image_copy = self.image
        self.rect = self.bullet.get_rect()
        self.rect.x, self.rect.y = px, py
        self.x, self.y = x, y
        self.name = name
        self.dad = dad
        self.op_dmg = 0

    def update(self, player):

        if self.rect.x < -65 or self.rect.x > 715 or self.rect.y < -65 or self.rect.y > 715:
            self.kill()

        if pygame.sprite.spritecollideany(self, opponents_sprites):
            if self.name == 'player':
                pygame.sprite.spritecollideany(self, opponents_sprites).health -= player.damage
                print(pygame.sprite.spritecollideany(self, opponents_sprites).health)
            if pygame.sprite.spritecollideany(self, opponents_sprites).health <= 0:
                x, y = pygame.sprite.spritecollideany(self, opponents_sprites).pos
                map_board[x][y] = 0
                pygame.sprite.spritecollideany(self, opponents_sprites).kill()
                dead_opponent.play()
            if self.name == 'player' or (self.name == 'opponent' and
                                       not(pygame.sprite.spritecollideany(self, opponents_sprites) is self.dad)):
                self.kill()
        if pygame.sprite.spritecollideany(self, player_sprite):
            if self.name == 'opponent':
                player.health -= self.op_dmg
                self.kill()
            if player.health <= 0:
                player.kill()
                dead_player.play()
                Flag = True


        if self.x == 1 or self.x == -1:
            self.rect.x += 2 * self.x
        if self.y == 1 or self.y == -1:
            self.rect.y += 2 * self.y

        if pygame.sprite.spritecollideany(self, wall_sprites):
            self.kill()



        # придумать проверку на столкновение нужно

    # def draw(self):
    #     pygame.draw.circle(screen, 'yellow', (self.px, self.py), 2)
        # можно не фото взять а рисовать , но замкнутый круг получится