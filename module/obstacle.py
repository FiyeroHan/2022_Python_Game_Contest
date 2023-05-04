import pygame
from random import randint
from module.game_data import levels

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, current_level):
        super().__init__()


        if type == 'long_bttm':
            self.image = pygame.image.load(levels[current_level]['obstacle'][0]).convert_alpha()
            y_pos = 720-230
        
        elif type == 'long_top':
            self.image = pygame.image.load(levels[current_level]['obstacle'][1]).convert_alpha()
            y_pos = 0
        
        elif type == 'short_bttm':
            self.image = pygame.image.load(levels[current_level]['obstacle'][2]).convert_alpha()
            y_pos = 720-152

        elif type == 'short_top':
            self.image = pygame.image.load(levels[current_level]['obstacle'][3]).convert_alpha()
            y_pos = 0

        self.rect = self.image.get_rect(midtop = (randint(1300,1500), y_pos))


    def destroy(self):
        if self.rect.x <= -200:
            self.kill()

    def update(self):
        self.rect.x -= 5
        self.destroy()
