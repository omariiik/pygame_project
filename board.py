import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)] # massiv
        self.board[0][0] = 1 # позиция игрока(0 пусто, 1 игрок, 2 противник, 3 стена)
        self.left = 0
        self.top = 0
        self.cell_size = 100

    def render(self, screen):
        # сюда вставишь update - ы своего класса
        pass