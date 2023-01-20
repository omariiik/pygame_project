import pygame
pygame.mixer.pre_init(44100, -16, 1, 512) # важно прописать до pygame.init()
pygame.init()
hay = pygame.mixer.Sound('data/o-privet.ogg')
marsh = 'data/marsh.mp3'
dead_opponent = pygame.mixer.Sound('data/nope.ogg')
dead_player = pygame.mixer.Sound('data/fiasko.ogg')
fon = 'data/фон.mp3'