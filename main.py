import pygame
import time
from board import Board
from tank import Tank
from game_map import map_board
from wall import Wall
from tank2 import Tank2
from bullet import Bullet
from sprites_groups import player_sprite
from sprites_groups import wall_sprites
from sprites_groups import opponents_sprites
from sprites_groups import bullet_group
from sprites_groups import Flag
from play_client import play_client
from music import hay, marsh


FPS = 30
SPEED = 20

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Танчики")
    size = 650, 650
    screen = pygame.display.set_mode(size)
    bg = pygame.image.load("data/пол.png")
    board = Board(10, 10)
    game_time = time.time()
    start_photo = pygame.image.load("data/startt.png")
    end_photo = pygame.image.load("data/end.png")

    for i in range(len(map_board)):
        for j in range(len(map_board)):
            if map_board[i][j] == 1:
                player = Tank(j * 65, i * 65)
                player_sprite.add(player)
            if map_board[i][j] == 2:
                obj = Wall(j * 65, i * 65)
                wall_sprites.add(obj)
            if map_board[i][j] == 3:
                opponent = Tank2(j * 65, i * 65)
                opponents_sprites.add(opponent)

    flag = False
    count = 0
    running = True
    p = 0
    while running:
        if count == 0:
            screen.blit(start_photo, (0, 0))
            if p == 0:
                hay.play()
                p += 1
                time.sleep(0.7)
                pygame.mixer.music.load(marsh)
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_1:
                        level = 1
                        flag = True
                        logic = 'random'
                        count += 1
                    elif event.key == pygame.K_2:
                        level = 2
                        flag = True
                        logic = 'logic'
                        count += 1
                    elif event.key == pygame.K_3:
                        level = 3
                        flag = True
                        logic = 'logic'
                        count += 1

        screen.blit(start_photo, (0, 0))
        if flag == True:
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player.move(0, -1, player.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player.move(0, 1, player.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.move(-1, 0, player.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        player.move(1, 0, player.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.shot()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        opponent.move(0, -1, opponent.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        opponent.move(0, 1, opponent.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        opponent.move(-1, 0, opponent.number_cell())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        opponent.move(1, 0, opponent.number_cell())
            screen.blit(bg, (0, 0))
            player_sprite.update()
            player_sprite.draw(screen)
            bullet_group.update(player)
            bullet_group.draw(screen)
            opponents_sprites.update()
            opponents_sprites.draw(screen)
            wall_sprites.draw(screen)
            for i in opponents_sprites:
                i.bot_brain()
            play_client(level)
            if len(player_sprite.sprites()) == 0:
                screen.blit(end_photo, (0, 0))


        pygame.display.flip()
    pygame.quit()