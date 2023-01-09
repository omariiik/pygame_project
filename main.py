import pygame
from board import Board
from tank import Tank
from game_map import map_board
from wall import Wall
FPS = 60
SPEED = 20

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Танчики")
    size = 650, 650
    screen = pygame.display.set_mode(size)
    bg = pygame.image.load("data/пол.png")
    board = Board(10, 10)

    all_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    for i in range(len(map_board)):
        for j in range(len(map_board)):
            if map_board[i][j] == 1:
                player = Tank(j * 65, i * 65)
                all_sprites.add(player)
            if map_board[i][j] == 2:
                obj = Wall(j * 65, i * 65)
                wall_sprites.add(obj)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        screen.blit(bg, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        wall_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
