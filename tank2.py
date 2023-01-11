import pygame
from game_map import map_board


class Tank2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.tank2 = pygame.image.load("data/tank2.png").convert_alpha()
        self.tank2_left = pygame.transform.flip(self.tank2, True, False) # танк перевёрнутый
        self.image = self.tank2
        self.image_copy = self.image
        self.rect = self.tank2.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score = 0
        self.back = False
        self.x = 0
        self.y = 0

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
                self.image = pygame.transform.rotate(self.image_copy, -90)
                if self.number_cell()[0] == 9:
                    self.x = 0
                elif self.start_pos[0] < 9 and not(map_board[self.start_pos[1]][self.start_pos[0] + 1] == 0):
                    self.x = 0
                else:
                    map_board[self.start_pos[1]][self.start_pos[0] + 1] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0
            elif self.x == -1 and self.y == 0:
                self.image = pygame.transform.rotate(self.image_copy, 90)
                if self.number_cell()[0] == 0:
                    self.x = 0
                elif self.start_pos[0] > 0 and not(map_board[self.start_pos[1]][self.start_pos[0] - 1] == 0):
                    self.x = 0
                else:
                    map_board[self.start_pos[1]][self.start_pos[0] - 1] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0
            elif self.x == 0 and self.y == 1:
                self.image = pygame.transform.rotate(self.image_copy, 180)
                if self.number_cell()[1] == 9:
                    self.y = 0
                elif self.start_pos[1] < 9 and not(map_board[self.start_pos[1] + 1][self.start_pos[0]] == 0):
                    self.y = 0
                else:
                    map_board[self.start_pos[1] + 1][self.start_pos[0]] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0
            elif self.x == 0 and self.y == -1:
                self.image = self.image_copy
                if self.number_cell()[1] == 0:
                    self.y = 0
                elif self.start_pos[1] > 0 and not(map_board[self.start_pos[1] - 1][self.start_pos[0]] == 0):
                    self.y = 0
                else:
                    map_board[self.start_pos[1] - 1][self.start_pos[0]] = 1
                    map_board[self.start_pos[1]][self.start_pos[0]] = 0

    def number_cell(self):
        return self.rect.x // 65, self.rect.y // 65

    def up_score(self): # рекорд
        self.score += 1
        # self.score_sound.play() # звук рекорда (потом сделаем)