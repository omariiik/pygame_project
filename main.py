import pygame
from board import Board
from tank import Tank
from wall import Wall

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Танчики")
    size = 650, 650
    screen = pygame.display.set_mode(size)
    bg = pygame.image.load("data/пол.png")
    board = Board(6, 6)
    FPS = 60
    speed = 20
    all_sprites = pygame.sprite.Group()
    player = Tank()
    all_sprites.add(player)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Tank.move(all_sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    Tank.move(all_sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    Tank.move(all_sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Tank.move(all_sprites)
        screen.blit(bg, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()