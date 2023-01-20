import pygame
from game_map import map_board
from bullet import Bullet
from sprites_groups import bullet_group
from sprites_groups import player_sprite
from bot_brain import random_brain
from bot_brain import logic
import time


class Tank2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/противник.png").convert_alpha()
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.health = 100
        self.damage = 25
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        self.back = False
        self.past_click = (0, -1)
        self.x = 0
        self.y = 0
        self.brain = 'random'
        self.start_time = time.time()
        self.past_move = 0
        self.pos = (x // 65, y // 65)

    def update(self, *args):
        if self.x == 1:
            if self.rect.x == (self.start_pos[0] + 1) * 65:
                self.x = 0
            else:
                self.rect.x += 1
        if self.y == 1:
            if self.rect.y == (self.start_pos[1] + 1) * 65:
                self.y = 0
            else:
                self.rect.y += 1
        if self.x == -1:
            if self.rect.x == (self.start_pos[0] - 1) * 65:
                self.x = 0
            else:
                self.rect.x -= 1
        if self.y == -1:
            if self.rect.y == (self.start_pos[1] - 1) * 65:
                self.y = 0
            else:
                self.rect.y -= 1

    def move(self, x, y, start_pos):
        if self.x == 0 and self.y == 0:
            self.x = x
            self.y = y
            self.start_pos = start_pos
            if self.x == 1 and self.y == 0:
                self.past_click = (1, 0)
                self.image = pygame.transform.rotate(self.image_copy, -90)
                if self.number_cell()[0] == 9:
                    self.x = 0
                elif self.start_pos[0] < 9 and not(map_board[self.start_pos[1]][self.start_pos[0] + 1] == 0):
                    self.x = 0
                else:
                    self.pos = (self.start_pos[1], self.start_pos[0] + 1)
                    map_board[self.start_pos[1]][self.start_pos[0] + 1] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0

            elif self.x == -1 and self.y == 0:
                self.past_click = (-1, 0)
                self.image = pygame.transform.rotate(self.image_copy, 90)
                if self.number_cell()[0] == 0:
                    self.x = 0
                elif self.start_pos[0] > 0 and not(map_board[self.start_pos[1]][self.start_pos[0] - 1] == 0):
                    self.x = 0
                else:
                    self.pos = (self.start_pos[1], self.start_pos[0] - 1)
                    map_board[self.start_pos[1]][self.start_pos[0] - 1] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0

            elif self.x == 0 and self.y == 1:
                self.past_click = (0, 1)
                self.image = pygame.transform.rotate(self.image_copy, 180)
                print(self.start_pos[1] - 1, self.start_pos[0])

                if self.number_cell()[1] == 9:
                    self.y = 0
                elif self.start_pos[1] < 9 and not(map_board[self.start_pos[1] + 1][self.start_pos[0]] == 0):
                    self.y = 0
                else:
                    self.pos = (self.start_pos[1] + 1, self.start_pos[0])
                    map_board[self.start_pos[1] + 1][self.start_pos[0]] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0

            elif self.x == 0 and self.y == -1:
                self.past_click = (0, -1)
                self.image = self.image_copy
                if self.number_cell()[1] == 0:
                    self.y = 0
                elif self.start_pos[1] > 0 and not(map_board[self.start_pos[1] - 1][self.start_pos[0]] == 0):
                    self.y = 0
                else:
                    self.pos = (self.start_pos[1] - 1, self.start_pos[0])
                    map_board[self.start_pos[1] - 1][self.start_pos[0]] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0


    def shot(self):
        if self.number_cell()[0] == 0 and self.past_click[0] == -1:
            return
        if self.number_cell()[0] == 9 and self.past_click[0] == 1:
            return
        if self.number_cell()[1] == 0 and self.past_click[1] == -1:
            return
        if self.number_cell()[1] == 9 and self.past_click[1] == 1:
            return
        if self.past_click[0] == 0 and self.past_click[1] == -1:
            obj = Bullet(self.rect.x + 25, self.rect.y - 15, 0, -1, 'opponent', self)
            obj.op_dmg = self.damage
            bullet_group.add(obj)
        if self.past_click[0] == 0 and self.past_click[1] == 1:
            obj = Bullet(self.rect.x + 28, self.rect.y + 50, 0, 1, 'opponent', self)
            obj.op_dmg = self.damage
            obj.image = pygame.transform.rotate(obj.image_copy, 180)
            bullet_group.add(obj)
        if self.past_click[0] == 1 and self.past_click[1] == 0:
            obj = Bullet(self.rect.x + 50, self.rect.y + 25, 1, 0, 'opponent', self)
            obj.op_dmg = self.damage
            obj.image = pygame.transform.rotate(obj.image_copy, -90)
            bullet_group.add(obj)
        if self.past_click[0] == -1 and self.past_click[1] == 0:
            obj = Bullet(self.rect.x - 10, self.rect.y + 25, -1, 0, 'opponent', self)
            obj.op_dmg = self.damage
            obj.image = pygame.transform.rotate(obj.image_copy, 90)
            bullet_group.add(obj)

    def ratio(self, rat):
        self.health += rat
        self.damage += rat // 2

    def number_cell(self):
        return self.rect.x // 65, self.rect.y // 65

    def up_score(self): # рекорд
        self.score += 1     # sound.play() # звук рекорда (потом сделаем)

    def bot_brain(self):
        if self.brain == 'random':
            random_brain(self)
        elif self.brain == 'logic':
            if len(player_sprite.sprites()) == 1:
                player = player_sprite.sprites()[0]
                logic(self, player)
