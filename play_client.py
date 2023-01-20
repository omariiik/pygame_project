from game_map import map_board
from tank2 import Tank2
from sprites_groups import opponents_sprites
import random
import pygame
m = 1
z = 1
g = 1
boss = 1
ratio1 = 0
ratio2 = 0
ratio3 = 0


def play_client(level):
    global m, ratio1
    if level == 1:
        n = len(opponents_sprites)
        if len(opponents_sprites.sprites()) < m:
            n = len(opponents_sprites.sprites())
            if m < 5:
                m += 1
            if m == 5:
                ratio1 += 5
                for i in opponents_sprites.sprites():
                    i.ratio(ratio1)
        i = n
        while i < m:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if map_board[y][x] == 0:
                obj = Tank2(x * 65, y * 65)
                opponents_sprites.add(obj)
                map_board[y][x] = 3
                i += 1
                n += 1
    if level == 2:
        global z, ratio2
        n = len(opponents_sprites)
        if len(opponents_sprites.sprites()) < z:
            n = len(opponents_sprites.sprites())
            if z < 3:
                z += 1
            if z == 3:
                ratio2 += 5
                for i in opponents_sprites.sprites():
                    i.ratio(ratio2)
        i = n
        while i < z:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if map_board[y][x] == 0:
                obj = Tank2(x * 65, y * 65)
                obj.brain = 'logic'
                opponents_sprites.add(obj)
                map_board[y][x] = 3
                i += 1
                n += 1
    if level == 3:
        global ratio3, g
        n = len(opponents_sprites.sprites())
        if len(opponents_sprites.sprites()) == 0 and g == 1:
            g = 0
            k = 0
            while k < 2:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if map_board[y][x] == 0:
                    obj = Tank2(x * 65, y * 65)
                    obj.brain = 'logic'
                    opponents_sprites.add(obj)
                    map_board[y][x] = 3
                    k += 1
        if len(opponents_sprites.sprites()) == 0 and g == 0:
            g = 3
            k = 0
            while k < 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if map_board[y][x] == 0:
                    obj = Tank2(x * 65, y * 65)
                    obj.image = pygame.image.load("data/БОСС.png").convert_alpha()
                    obj.image_copy = obj.image
                    obj.brain = 'logic'
                    obj.health = 200
                    obj.damage = 40
                    opponents_sprites.add(obj)
                    map_board[y][x] = 3
                    k += 1
        if len(opponents_sprites.sprites()) == 0 and g == 3:
            k = 0
            while k < 1:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if map_board[y][x] == 0:
                    obj = Tank2(x * 65, y * 65)
                    obj.image = pygame.image.load("data/БОСС.png").convert_alpha()
                    obj.image_copy = obj.image
                    obj.brain = 'logic'
                    obj.health = 200
                    obj.damage = 40
                    obj.ratio(ratio3)
                    opponents_sprites.add(obj)
                    map_board[y][x] = 3
                    k += 1