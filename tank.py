import pygame


class Tank(pygame.sprite.Sprite):
    # score_sound = pygame.mixer.Sound(get_path('дорога к звуку'))
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tank1 = pygame.image.load("data/танк+90.png").convert_alpha()
        self.tank1_left = pygame.transform.flip(self.tank1, True, False) # танк перевёрнутый
        self.image = self.tank1
        self.rect = self.tank1.get_rect()
        self.score = 0
        self.back = False
        # self.score_sound.set_volume(0.2)

    def update(self, *args):
        # если танк выйдет за границу, то он будет переворачиваться и идти в обратную сторону
        if self.rect.x <= 585 and self.back:
            self.image = self.tank1
        if self.rect.x == 0 and self.back:
            self.back = False
        if self.rect.x == 585:
            self.back = True

    def move(self):
        # движение танка, нужно учитывать то, что в update
        pass

    def up_score(self): # рекорд
        self.score += 1
        # self.score_sound.play() # звук рекорда (потом сделаем)